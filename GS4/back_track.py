'''
Swetha Sankar
Lesson 19: Backtracking
April 20, 2021
Cracked Password: AdaIsGoodDog
'''
from __future__ import annotations

import sys
from zipfile import Path
from GS4.password_hash import simple_hash
global TEXT


def search_zip(folder: Path, file_type: str) -> list[Path]:
    """
    Recursively search a zip file by iterating through its files and subfolders.
    Paths are basically just fancy strings with some extra features, like checking
    if they are directories or files.
    Args:
        folder (Path): A ZipFile Path that represents a folder.
        file_type (str): The extension to check against the individual files
    Returns:
        list[Path]: All the matched Paths
    """
    result = []
    for folder_item in folder.iterdir():
        # Is it a directory?
        if folder_item.is_dir():
            result.extend(search_zip(folder_item, file_type))
        # Is it a file?
        if folder_item.is_file():
            if folder_item.name.endswith(file_type):
                result.append(folder_item)
    return result


def appending(lst: [str]) -> str:
    # short function to append strings in list into one string
    result = ""
    for string in lst:
        result += string
    return result


def backtrack(n, k, depth, curr, ans):
    '''
    function to generate all combinations of the dictionary with size k
    :param n: int length of dictionary (46)
    :param k: int subset size (increment in main)
    :param depth: int current size
    :param curr: [str] current password attempt order
    :param ans: [str] potential answer
    :return:
    '''
    if depth == k:  # potential candidate
        ans.append(curr[::])
        return

    for i in range(n):
        curr.append(TEXT[i])
        backtrack(n, k, depth + 1, curr, ans)
        curr.pop()
    return


if __name__ == '__main__':
    # Load the Zip File
    ZIP_FILE_NAME = 'GS4/mysterious_drive.zip'
    root = Path(ZIP_FILE_NAME)
    # Search the Zip File to find password_hash.py & dictionary.txt
    pass_hash = search_zip(root, ".py")[0]
    # print(pass_hash)
    # mysterious_drive.zip/c/Home/atb/lib/usr/password_hash.py
    with open('GS4/dictionary.txt') as data_file:
        TEXT = data_file.readlines()
    i = 0
    for line in TEXT:
        TEXT[i] = line.rstrip()
        i += 1

    n = len(TEXT)
    ans = []

    for i in range(len(TEXT)):
        # use the backtrack algorithm in subsets
        # (ex. go through all combos of size i while i < the size of the dictionary)
        backtrack(n, i, 0, [], ans)
        for i in ans:
            if simple_hash(appending(i), 10 ** 9) == 81445731:
                print(appending(i))
                # stop program execution after you find this line
                sys.exit()


'''
1st attempt :(
def backtrack(current_pass, lst:[str], current_size: int) -> [str]:
    max_size = 46
    if current_size > max_size:
        return
    if simple_hash(appending(lst), 10**9) == 81445731:
        ans.append(lst[::])
        return lst
    # Else construct next candidates
    else:
        trying = ""
        possible_pass = [word for word in TEXT if word not in lst]
        final_result = []
        for potential in possible_pass:
            lst.append(potential)
            # recursive call
            result = backtrack(lst, current_size+1)
            final_result.extend(result)
            lst.pop()
        return final_result
'''



