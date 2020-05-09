from typing import List, Iterator


def get_alphanumericals_and_comma():
    for i in range(128):
        if chr(i).isalnum() or chr(i) == ',':
            yield chr(i)


def get_self_loops(i: int) -> List[str]:
    return ["%i %s %i" % (i, lo, i) for lo in get_alphanumericals_and_comma()]


def get_all_self_loops(n: int = 13) -> List[str]:
    return [i for j in range(n) for i in get_self_loops(j)]


def get_all_comma_trans(n: int = 13) -> List[str]:
    return ["%i , %i" % (i, i + 1) for i in range(n - 1)]


def get_regex_trans(n: int = 13) -> List[str]:
    return get_all_comma_trans(n) + get_all_self_loops(n) + ["%i z %i" % (n - 1, n)]


def write_into_file(file: str, data: Iterator[str]) -> None:
    with open(file, 'w+') as f:
        for item in data:
            f.write("%s\n" % item)


if __name__ == '__main__':
    n = 13
    file = "2020_H12.trans"
    # First rule is for implementation from last week, second rule is for word epsilon
    regex_trans: Iterator[str] = filter(lambda x: len(x.split()) == 3 and x.split()[1] != '',
                                        get_regex_trans(n))
    write_into_file(file, regex_trans)
