import os
import re

from timeit import default_timer as timer
from typing import List

regex_dir: str = 'regex.txt'
regex_test_dir: str = 'regex_tests/'


def load_file(file: str) -> str:
    """
    Loads file and returns first line
    :param file: path to file
    :return: Content of first line of file
    """
    with open(file) as f:
        line: str = f.readlines()[0]
    return line


def test_regex(file: str, regex: str):
    """

    :param file:
    :param regex:
    :return:
    """
    print(file)
    start: timer = timer()
    line: str = load_file(file)
    line: List[str] = re.findall(regex, line)
    print(line)
    end: timer = timer()
    print("It took")
    print("%f" % (end - start))
    print("seconds.")
    print()


def test_all_regex(dire: str, regex: str):
    """

    :param dire:
    :param regex:
    :return:
    """
    for file in os.listdir(dire):
        print(file)
        test_regex(dire + file, regex)


if __name__ == "__main__":
    print("We start with an implementation from category 2 (Python) -----")
    regex: str = re.compile(load_file(regex_dir))
    test_all_regex(regex_test_dir, regex)
    print("Category 2 done -----")
