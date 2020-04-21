from type3 import load_dfa_from_json

import matplotlib.pyplot as plt


def test():
    dfa1 = load_dfa_from_json('data/dfa1.json')
    dfa2 = load_dfa_from_json('data/dfa2.json')
    # assert dfa.decide('aaabaaa')
    # assert not dfa.decide('aaabb')
    # g = dfa.get_graph()
    dfa2.product(dfa1)

    # plt.dra


if __name__ == "__main__":
    test()
