"""
Author: swetha@udel.edu
Date: 3/10/2021
Description: CISC 320 Lesson 09: Implementing an Algorithm
Calculate, sort, and report maximum, most recent, and average of a sequence of logs
Each line of output will contain four numbers:

The student's ID
The student's lowest Page ID
The student's latest Page ID
The student's average submission score (the sum of all the scores divided by the number of scores).
If a student doesn't have at least one submission and at least one page, then you should exclude it from the output.
The students should be sorted in ascending order based the status results:
first by their lowest page ID, than their latest page ID, and finally by their average score. Truncate any decimals to
become integers.
"""


def map_lines(lines: [str]):
    """
        Create dictionary of dictionaries for student IDS and corresponding info. Perform avg sub score, latest time,
         and minimum score operations before returning dict. Returns dictionary of dictionaries."""
    sids = dict()
    for line in lines[1:]:
        # format line split to make accessing elements easier

        sid, ty, val, time = line.split()
        # initialize array for the average sum score calculation
        current_time = 0

        # ignore anything with ty == 'T' (unnecessary for problem) & initialize dict of dicts!
        if sid not in sids and ty == 'P':
            sids[sid] = {'sid': sid, 'lowest_pid': val, 'latest_pid': val, 'sub_score': "na"}
            current_time = int(time)
        elif sid not in sids and ty == 'S':
            sids[sid] = {'sid': sid, 'lowest_pid': "na", 'latest_pid': "na", 'sub_score': val, 'running_sum': float(val), 'selms': 1}

        elif sid in sids:
            if sids[sid]['sub_score'] == "na" and ty == 'S':
                # First submission entry after a page entry
                sids[sid]['selms'] = 1.0
                sids[sid]['running_sum'] = float(val)
                sids[sid]['sub_score'] = str(val)

            elif sids[sid]['sub_score'] != "na" and ty == 'S':
                # Calculating average subscore & replacing current value w/ it
                sids[sid]['selms'] = sids[sid]['selms'] + 1.0
                sids[sid]['running_sum'] = sids[sid]['running_sum'] + float(val)
                sids[sid]['avg_value'] = float(sids[sid]['running_sum']/sids[sid]['selms'])
                sids[sid]['sub_score'] = str(int(sids[sid]['avg_value']))

            if sids[sid]['lowest_pid'] != "na" and ty == 'P':
                # Calculating minimum pid (compare subsequent pids to current pid)
                temp = int(sids[sid]['lowest_pid'])
                if int(val) < temp:
                    sids[sid]['lowest_pid'] = str(val)

            if sids[sid]['lowest_pid'] == "na" and ty == 'P':
                # Assigning first page entry pid
                sids[sid]['lowest_pid'] = val

            if (sids[sid]['latest_pid'] == "na") and (ty == 'P'):
                # If first page entry, then reassigns na value to time
                current_time = time
                sids[sid]['latest_pid'] = val

            if (sids[sid]['latest_pid'] != "na") and (ty == 'P'):
                # Updating latest_pid w/ most recent time
                temp1 = int(current_time)
                if int(time) > temp1:
                    sids[sid]['latest_pid'] = val

    return sids


def ascending_order(element):
    # method for sorting the final student id dictionary
    lowpid = element[1]['lowest_pid']
    latest = element[1]['latest_pid']
    sub = element[1]['sub_score']
    return lowpid, latest, sub


if __name__ == "__main__":
    # Get the filename from stdin
    filename = input()

    # Open the file and read in its contents
    with open(filename) as data_file:
        # O(L) operation
        files = data_file.readlines()

    # Actually do the work
    things = map_lines(files)
    sorted_dict = dict(sorted(things.items(), key=ascending_order))
    for item in sorted_dict.keys():
        if sorted_dict[item]['lowest_pid'] != 'na' and sorted_dict[item]['latest_pid'] != 'na' \
                and sorted_dict[item]['sub_score'] != 'na':
            # don't print any students that don't have at least one submission or at least one page!
            print(item + " " + sorted_dict[item]['lowest_pid'] + " " + sorted_dict[item]['latest_pid'] + " " +
                  sorted_dict[item]['sub_score'])
