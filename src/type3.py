from typing import Set, Optional, Callable
# from itertools.chain import from_iterable

from networkx import MultiDiGraph

from utils.file_tools import load_json

import matplotlib.pyplot as plt
import itertools as it


class Automata:
    pass


class State:
    def __init__(self, name: str = None):
        self.name: str = name

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return str(self.name)


class Transition:
    def __init__(self):
        pass


class DFA(Automata):

    def __init__(self, Q: Set[State], Sigma: Set[str], delta: Callable[[State, str], State], q_0: State,
                 F: Set[State]):
        self.Q: Set[State] = Q  # All states
        self.q_0: State = q_0  # Starting state
        self.F: Set[State] = F  # Final states
        self.delta: Callable[[State, str], State] = delta  # Transition function
        self.Sigma: Set[str] = Sigma  # Input words
        if not self.validate():
            raise Exception

    def validate(self) -> bool:
        """
        Returns, if DFA is defined correctly
        :return: DFA is defined correctly or not
        """
        if not {self.q_0}.union(self.F) <= self.Q:
            # Check if both starting state and end states are in Q
            print('this')
            return False
        # Check if transition function is valid
        for state in self.Q:
            for word in self.Sigma:
                if self.delta(state, word) not in self.Q:
                    print('that')
                    return False
        return True

    def get_graph(self) -> MultiDiGraph:
        g: MultiDiGraph = MultiDiGraph()
        g.add_nodes_from(map(lambda x: str(x), self.Q))

        return g


class PartialDFA(DFA):

    def __init__(self, Q: Set[State], Sigma: Set[str], delta: Callable[[State, str], Optional[State]], q_0: State,
                 F: Set[State]):
        self.Q: Set[State] = Q  # All states
        self.q_0: State = q_0  # Starting state
        self.F: Set[State] = F  # Final states
        self.delta: Callable[[State, str], Optional[State]] = delta  # Transition function
        self.Sigma: Set[str] = Sigma  # Input words
        if not self.validate():
            raise Exception

    def validate(self) -> bool:
        """
        Returns, if DFA is defined correctly
        :return: DFA is defined correctly or not
        """
        if not {self.q_0}.union(self.F) <= self.Q:
            # Check if both starting state and end states are in Q
            return False
        # Check if transition function is valid
        for state in self.Q:
            for word in self.Sigma:
                if self.delta(state, word) not in self.Q:
                    return False
        return True


def load_dfa_from_json(file: str) -> DFA:
    dfa_obj = load_json(file)
    Q: Set[State] = set(map(State, dfa_obj.keys()))
    Sigma: Set[str] = set(it.chain.from_iterable([state['transitions'].keys() for _, state in dfa_obj.items()]))
    F: Set[State] = set(map(State, [state for state, values in dfa_obj.items() if values['final_state']]))
    q_0: Optional[State] = set(
        map(State, [state for state, values in dfa_obj.items() if 'starting_state' in values.keys()])).pop()
    delta: Callable[[State, str], State] = lambda state, entry: State(
        dfa_obj.get(str(state), {'transitions': {}})['transitions'].get(entry, None))

    return DFA(Q, Sigma, delta, q_0, F)
