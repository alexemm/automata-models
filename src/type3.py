from typing import Set, Optional, Callable

from networkx import MultiDiGraph, draw, spring_layout
from networkx.drawing.nx_agraph import to_agraph

from utils.file_tools import load_json, save_json

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

    def decide(self, word: str) -> bool:
        run = self.q_0
        for char in word:
            run = self.delta(run, char)
        return run in self.F

    def __neg__(self):
        return self.complement()

    def complement(self):
        return DFA(self.Q, self.Sigma, self.delta, self.q_0, self.Q - self.F)

    def product(self, other, mode='intersection'):
        new_states = [(state1, state2) for state1, state2 in it.product(self.Q, other.Q)]
        state_name = lambda state1, state2: "(%s, %s)" % (str(state1), str(state2))
        delta_dict = {state_name(state1, state2): {'transitions': {}} for state1, state2 in new_states}
        for state1, state2 in new_states:
            if state1 == self.q_0 and state2 == other.q_0:
                delta_dict[str(State(state_name(state1, state2)))]['starting_state'] = True
            if mode == 'intersection':
                delta_dict[str(State(state_name(state1, state2)))][
                    'final_state'] = state1 in self.F and state2 in other.F
            else:
                delta_dict[str(State(state_name(state1, state2)))][
                    'final_state'] = state1 in self.F or state2 in other.F
            for entry in self.Sigma:
                delta_dict[str(State(state_name(state1, state2)))]['transitions'][entry] = str(
                    State(state_name(self.delta(state1, entry), other.delta(state2, entry))))
        # save_json('data/dfa3.json', delta_dict)
        return load_dfa_from_dict(delta_dict)

    def __mul__(self, other):
        return self.product(other)

    def __rmul__(self, other):
        return self.product(other)

    def __imul__(self, other):
        return self.product(other)

    def get_graph(self):
        g: MultiDiGraph = MultiDiGraph()
        for node in self.Q:
            color = 'black'
            if node in self.F:
                color = 'red'
            g.add_node(str(node), color=color)
        g.add_nodes_from(map(str, self.Q))
        for state in self.Q:
            next_states = set([self.delta(state, entry) for entry in self.Sigma])
            next_states_transitions = [
                (next_state, ', '.join([entry for entry in self.Sigma if self.delta(state, entry) == next_state])) for next_state in
                next_states]
            for next_state, entry in next_states_transitions:
                g.add_edge(state, next_state, label=entry)
        plt.figure()
        g.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
        g.graph['graph'] = {'scale': '3'}
        A = to_agraph(g)
        A.layout('dot')
        return A

    def save_graph(self, file: str):
        self.get_graph().draw(file)


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


def load_dfa_from_dict(dfa_obj) -> DFA:
    Q: Set[State] = set(map(State, dfa_obj.keys()))
    Sigma: Set[str] = set(it.chain.from_iterable([state['transitions'].keys() for _, state in dfa_obj.items()]))
    F: Set[State] = set(map(State, [state for state, values in dfa_obj.items() if values['final_state']]))
    q_0: Optional[State] = set(
        map(State, [state for state, values in dfa_obj.items() if 'starting_state' in values.keys()])).pop()
    delta: Callable[[State, str], Optional[State]] = lambda state, entry: State(
        dfa_obj.get(str(state), {'transitions': {}})['transitions'].get(entry, None)) if state is not None else None

    return DFA(Q, Sigma, delta, q_0, F)


def load_dfa_from_json(file: str) -> DFA:
    dfa_obj = load_json(file)
    return load_dfa_from_dict(dfa_obj)
