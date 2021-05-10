"""
Simplistic hashing function for turning a string into a number.
By storing the number instead of the string, we can check that a given password
matches the expected one, without storing the plain text password.
Make sure no one besides me gets access to this source code!

Hashed password: 81445731
"""


def simple_hash(a_string: str, maximum_value: int) -> int:
    """
    Hashes a string value to produce a semi-unique integer.

    Args:
        a_string (str): Any string value that you want to hash.
        maximum_value (int): The maximum value of the hashed result, used as a modulus.
    Returns:
        int: The generated hash code of the string.
    """
    summation = 0
    multiplicand = 1
    for character in a_string:
        multiplicand = (multiplicand * 3) % maximum_value
        summation += (ord(character) * multiplicand) % maximum_value
    return int(abs(summation) % maximum_value)
