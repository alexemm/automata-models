from typing import TypeVar, Hashable, List, Tuple

# Everything which can be stored in a set
A: TypeVar = TypeVar('A', bound=Hashable)
S: TypeVar = TypeVar('S', bound=Hashable)


def load_transitions(file: str) -> List[Tuple[S, A, S]]:
    """
    Loads .trans-file in form of "State Symbol State" for every line.
    :param file: path to file
    :return: List of tuples which are used as arguments
    """
    with open(file) as f:
        lines: List[Tuple[S, A, S]] = list(
            map(lambda x: (int(x.split()[0]), str(x.split()[1]), int(x.split()[2])), f.readlines()))
    return lines


def load_words(file: str) -> List[str]:
    """
    Loads words from input file.
    :param file: path to file
    :return:
    """
    with open(file) as f:
        words: List[str] = f.readlines()
    return words
