from type3 import load_dfa_from_json


def test():
    dfa = load_dfa_from_json('data/dfa1.json')
    assert dfa.decide('aaabaaa')
    assert not dfa.decide('aaabb')
    import pdb;
    pdb.set_trace()


if __name__ == "__main__":
    test()
