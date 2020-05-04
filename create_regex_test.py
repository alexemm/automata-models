import os
from typing import List


def get_w_i(i: int) -> str:
    """
    Returns string in form of 1,2,...,12,1,..1 depending on how many 1s should be appended to the end
    :param i: Number of 1s in the end of the string
    :return: String output
    """
    return "%s" % ','.join([str(i) for i in range(1, 13)] + (["1"] * i))


def create_test(n: int = 20, dire: str = "regex_tests/") -> None:
    """
    Creates test directory for regex testing later on.
    :param n: Number of 1s to append in the file
    :param dire: Directory where all test cases are stored
    :return: None
    """
    testcases: List[str] = [get_w_i(i) for i in range(1, 21)]
    if not os.path.exists(dire):
        os.mkdir(dire)
    for i, testcase in enumerate(testcases):
        save_file(dire + str(i + 1).zfill(len(str(n))), testcase)


def save_file(file: str, data: str) -> None:
    """
    Saves data in given file
    :param file: path to file (creates new file if it does not exist)
    :param data: Data to save in string format
    :return: None
    """
    with open(file, 'w+') as f:
        f.write(data)


if __name__ == '__main__':
    create_test(20)
