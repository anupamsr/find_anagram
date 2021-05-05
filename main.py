import datetime
import io
import random
from contextlib import redirect_stdout

from prefix_tree import SortedPrefixTree


class Timer(list):
    def __init__(self, function):
        super().__init__()
        self.function = function

    def __call__(self, *args, **kwargs):
        f = io.StringIO()
        with redirect_stdout(f):
            start_time = datetime.datetime.utcnow()
            res = self.function(*args, **kwargs)
            end_time = datetime.datetime.utcnow()
        out = f.getvalue()
        if len(out) != 0:
            print(f"[{end_time - start_time}] {out}", end='')
        else:
            print(f"[{end_time - start_time}] {self.function}")
        return res


@Timer
def find_word(pt: SortedPrefixTree, word: str):
    matches = pt.get_matches(word)
    if len(matches) == 0:
        print(f"not found: {word}")
    else:
        print(f"{word} has following anagrams:")
        for match in matches:
            print(match)


def create_string(n: int) -> str:
    word = str()
    for j in range(0, n):
        word += chr(ord('a') + random.randint(0, 25))
    return word


@Timer
def create_pt(n: int, m: int) -> SortedPrefixTree:
    pt = SortedPrefixTree(["lowercase", "str", "object", "has", "no", "attribute", "found", "not",
                           "python", "ahs"])
    for i in range(0, m):
        pt.add_word(create_string(n))
    return pt


def main():
    n = 4  # Average length of the string
    m = 10000  # Total number of strings
    pt = create_pt(n, m)
    for i in range(0, 100):
        find_word(pt, create_string(n))

    find_word(pt, "tac")
    find_word(pt, "tca")
    find_word(pt, "acn")
    find_word(pt, "tab")
    find_word(pt, "sah")
    find_word(pt, "shab")


if __name__ == "__main__":
    main()
