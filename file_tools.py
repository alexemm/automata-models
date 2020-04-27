from typing import List, Tuple


def load_transitions(file: str) -> List[Tuple[int, str, int]]:
    """
    Loads .trans-file in form of "State Symbol State" for every line.
    :param file: path to file
    :return: List of tuples which are used as arguments
    """
    with open(file) as f:
        lines: List[Tuple[int, str, int]] = list(
            map(lambda x: (int(x.split()[0]), str(x.split()[1]), int(x.split()[2])), f.readlines()))
    return lines


def load_words(file: str) -> List[str]:
    """
    Loads words from input file where there is a word in every line.
    :param file: path to file
    :return: List of words
    """
    with open(file) as f:
        words: List[str] = f.readlines()
    return words
