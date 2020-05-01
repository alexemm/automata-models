# Note: Type hints (typing lib) are introduced in Python 3.5, therefore use this version or newer (Tested with 3.7)
from typing import Set, List, Tuple, TypeVar, Hashable
from timeit import default_timer as timer

from nfa import NFA
from file_tools import load_transitions, load_words

# Everything which can be stored in a set
A: TypeVar = TypeVar('A', bound=Hashable)
S: TypeVar = TypeVar('S', bound=Hashable)


def do_simulation(M: NFA[S, A], zustand: S, eingabe: List[A], i: int = 0) -> None:
    """
    Does simulation on given NFA, measures time and prints the result from the simulation.
    :param M: NFA
    :param zustand: Current state
    :param eingabe: Word as list of A
    :param i:
    :return: None
    """
    print("NFA simulation started for case %i with length of %i" % (i, len(eingabe)))
    start: timer = timer()
    reachable: Set[S] = M.simulate(zustand, eingabe)
    end: timer = timer()
    print("Finished. It took %f seconds." % (end - start))
    print("The resulting set is:")
    print(reachable)


def test_nfa_1() -> None:
    """
    Test Case 1 is executed here. It covers the example case which was not mandatory.
    :return: None
    """
    print("Test Case 1 started ---")
    states: Set[int] = {1, 2, 3, 4}

    print("Transition addition runtime: Start")
    M: NFA[int, str] = NFA[int, str](states)
    start: timer = timer()
    M.addTransition(1, "rechts", 2)
    M.addTransition(1, "runter", 3)
    M.addTransition(2, "links", 1)
    M.addTransition(2, "runter", 4)
    M.addTransition(3, "rechts", 4)
    M.addTransition(3, "hoch", 1)
    M.addTransition(4, "links", 3)
    M.addTransition(4, "hoch", 2)
    end: timer = timer()
    print("Finished. It took %f seconds." % (end - start))

    eingabe: List[str] = ['rechts', 'runter', 'links']
    start_zustand = 1
    do_simulation(M, start_zustand, eingabe)

    print("Test Case 1 ended ---")


def load_and_create_nfa(transition_file: str) -> NFA[int, str]:
    """
    Creates NFA from given file.
    :return: NFA[int, str]
    """
    print("Creating NFA")
    nfa: NFA[int, str] = NFA[int, str](set(range(35)))
    transitions: List[Tuple[int, str, int]] = load_transitions(transition_file)
    print("Transition addition runtime: Start")
    start: timer = timer()
    for transition in transitions:
        nfa.add_transition(*transition)
    end: timer = timer()
    print("Finished. It took %f seconds.\n" % (end - start))
    return nfa


def test_nfa_2(nfa: NFA[S, A]) -> None:
    """
    The first test case from the home work is executed here. It just simulates the word 'abababbaa' on the given NFA.
    :param nfa: NFA
    :return: None
    """
    eingabe: str = 'abababbaa'
    print("Test Case 0 with word '%s' with length %s started ---" % (eingabe, len(eingabe)))
    eingabe: List[str] = list(eingabe)
    start_zustand = 7
    do_simulation(nfa, start_zustand, eingabe)
    print("Test Case 0 ended ---\n")


def test_nfa_3(nfa: NFA[S, A]) -> None:
    """
    Test cases from the homework. The words are loaded from the file and are simulated in the NFA
    :return: None
    """
    words_file: str = '2020_H09_input'
    start_zustand = 7
    print("Start testing simulation of words from file---")
    eingaben: List[List[str]] = list(map(list, load_words(words_file)))
    for i, eingabe in enumerate(eingaben):
        do_simulation(nfa, start_zustand, eingabe, i)
    print("Finished testing simulation ---")


if __name__ == '__main__':
    transition_file: str = '2020_H09.trans'
    nfa = load_and_create_nfa(transition_file)
    # test_nfa_1()
    test_nfa_2(nfa)
    test_nfa_3(nfa)
