from typing import Set, List, Tuple
from timeit import default_timer as timer

from nfa import NFA
from file_tools import load_transitions, load_words


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
    print("NFA simulation started")
    start: timer = timer()
    reachable: Set[int] = M.simulate(1, eingabe)
    end: timer = timer()
    print("Finished. It took %f seconds." % (end - start))
    print(reachable)

    print("Test Case 1 ended ---")


def test_nfa_23() -> None:
    """
    Test cases from the homework
    :return: None
    """
    transition_file: str = '2020_H09.trans'
    words_file: str = '2020_H09_input'
    print("Test Case 2 started ---")
    nfa: NFA[int, str] = NFA[int, str](set(range(35)))
    transitions: List[Tuple[S, A, S]] = load_transitions(transition_file)
    print("Transition addition runtime: Start")
    start: timer = timer()
    for transition in transitions:
        nfa.add_transition(*transition)
    end: timer = timer()
    print("Finished. It took %f seconds." % (end - start))

    eingabe: List[str] = list('abababbaa')
    print("NFA simulation started")
    start: timer = timer()
    reachable: Set[int] = nfa.simulate(7, eingabe)
    end: timer = timer()
    print("Finished. It took %f seconds." % (end - start))
    print(reachable)

    print("Test Case 2 ended ---")

    print("Test Case 3 started ---")
    eingaben: List[List[str]] = list(map(list, load_words(words_file)))
    for i, eingabe in enumerate(eingaben):
        print("NFA simulation started for case %i with length of %i in file" % (i, len(eingabe)))
        start: timer = timer()
        reachable: Set[int] = nfa.simulate(7, eingabe)
        end: timer = timer()
        print("Finished. It took %f seconds." % (end - start))
        print(reachable)

    print("Test Case 3 ended ---")


if __name__ == '__main__':
    test_nfa_1()
    test_nfa_23()
