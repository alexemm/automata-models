from typing import Set, Generic, TypeVar, Dict, List, Hashable

# Everything which can be stored in a set
A: TypeVar = TypeVar('A', bound=Hashable)
S: TypeVar = TypeVar('S', bound=Hashable)


class NFA(Generic[S, A]):
    """
    This class represents a Non-Deterministic Finite Automaton (NFA)
    """

    def __init__(self, Q: Set[S]):
        self.Q: Set[S] = Q  # Set of states
        self.transitions: Dict[S, Dict[A, Set[S]]] = {state: {} for state in self.Q}

    def add_transition(self, q: S, a: A, p: S) -> None:
        """
        Adds transition in NFA. This is done inplace.
        :param q: Initial State
        :param a: Transition symbol
        :param p: State where the transitions goes to
        :return: None
        """
        if q not in self.transitions.keys():
            self.transitions[q]: Dict[A, Set[S]] = {}
        if p not in self.transitions.keys():
            self.transitions[p]: Dict[A, Set[S]] = {}
        self.transitions[q][a]: Set[S] = self.transitions[q].get(a, set()).union({p})

    def addTransition(self, q: S, a: A, p: S) -> None:
        """
        Camel case function declaration since we need to use it in our homework (snail_case makes more sense in python
        tho). It just calls the add_transition method
        :param q: Initial State
        :param a: Transition symbol
        :param p: State where the transitions goes to
        :return: None
        """
        self.add_transition(q, a, p)

    def simulate(self, q: S, w: List[A], rek: bool = False) -> Set[S]:
        """
        This simulates the NFA with given word and state and calculates delta^hat(q, w).
        :param q: Starting state
        :param w: Word which is simulated
        :param rek: Uses the simple recursive way (Can cause MemoryError if w is too long)
        :return: All the states which are given in a set
        """
        if rek:
            ret: Set[S] = set()
            self.simulate_rek(q, w, ret)
            return ret
        else:
            ret: Set[S] = {q}
            for symbol in w:
                if len(ret) == 0:
                    return ret
                # Get all next states and assign it to ret
                union: Set[S] = set()
                for state in ret:
                    union: Set[S] = self.transitions[state].get(symbol, set()).union(union)
                ret: Set[S] = union
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
            return
        for next_state in self.transitions[q].get(w[0], []):
            self.simulate_rek(next_state, w[1:], ret)
