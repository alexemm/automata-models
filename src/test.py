from type3 import load_dfa_from_json


def test():
    dfa1 = load_dfa_from_json('data/dfa1.json')
    dfa2 = load_dfa_from_json('data/dfa2.json')
    # assert dfa1.decide('aaabaaa')
    # assert not dfa1.decide('aaabb')
    dfa3 = dfa2.product(dfa1)
    dfa1.save_graph('plots/dfa1.png')
    dfa2.save_graph('plots/dfa2.png')
    dfa3.save_graph('plots/dfa3.png')


if __name__ == "__main__":
    test()
