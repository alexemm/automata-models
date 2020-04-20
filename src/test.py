from type3 import load_dfa_from_json

import matplotlib.pyplot as plt

def test():
    dfa = load_dfa_from_json('data/dfa2.json')
    # assert dfa.decide('aaabaaa')
    # assert not dfa.decide('aaabb')
    g = dfa.get_graph()

    plt.dra

    import pdb;
    pdb.set_trace()


if __name__ == "__main__":
    test()
