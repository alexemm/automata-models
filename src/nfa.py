from typing import Set, Generic, TypeVar, Dict, List, Hashable

# Everything which can be stored in a set
A = TypeVar('A', bound=Hashable)
S = TypeVar('S', bound=Hashable)


class NFA(Generic[S, A]):
    """
    This class represents a Non-Deterministic Finite Automaton (NFA)
    """

    def __init__(self, Q: Set[S]):
        self.Q: Set[S] = Q  # Set of states
        self.transitions: Dict[S, Dict[A, Set[A]]] = {state: {} for state in self.Q}

    def add_transition(self, q: S, a: A, p: S) -> None:
        """
        Adds transition in NFA. This is done inplace.
        :param q: Initial State
        :param a: Transition symbol
        :param p: State where the transitions goes to
        :return: None
        """
        if q not in self.transitions.keys():
            raise Exception
        self.transitions[q][a]: Set[S] = self.transitions[q].get(a, set()).union(set(p))

    def simulate(self, q: S, w: List[A]) -> Set[S]:
        """
        This simulates the NFA with given word and state and calculates delta^hat(q, w) recursively using Dynamic
        Programming
        :param q: Starting state
        :param w: Word which is simulated
        :return: All the states which are given in a set
        """
        ret: Set[S] = set()
        self.simulate_rek(q, w, ret)
        return ret

    def simulate_rek(self, q: S, w: List[A], ret: Set[S]) -> None:
        """
        Helper method for simulation of NFA using Dynamic Programming.
        :param q: Starting state
        :param w: Word which is simulates
        :param ret: Dynamic set for return in main method
        :return: None
        """
        # To make it more efficient, since recursion is limited (All states are reached, that's it)
        if ret == self.Q:
            return
        # Termination condition
        if len(w) == 0:
            ret.add(q)
        for next_state in self.transitions[q][w[0]]:
            self.simulate_rek(next_state, w[1:], ret)
