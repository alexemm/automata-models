# Note: Type hints (typing lib) are introduced in Python 3.5, therefore use that version or newer (Tested with 3.7)
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
        :param p: State where the transitions go to
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
        :param p: State where the transitions go to
        :return: None
        """
        self.add_transition(q, a, p)

    def simulate(self, q: S, w: List[A]) -> Set[S]:
        """
        This simulates the NFA with given word and state and calculates delta^hat(q, w).
        :param q: Starting state
        :param w: Word which is simulated
        :return: All the states which are the output of the simulation in a set
        """
        run: Set[S] = {q}
        for symbol in w:
            if run == set():
                return run
            # Get all next states and update ret (List comps are more performing than for-loops (and pythonic))
            run: Set[S] = set().union(*[self.transitions[state_set].get(symbol, set()) for state_set in run])
        return run
