class Node:
    def __init__(self):
        self.words = list()
        self.leaves = {
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
            "g": None,
            "h": None,
            "i": None,
            "j": None,
            "k": None,
            "l": None,
            "m": None,
            "n": None,
            "o": None,
            "p": None,
            "q": None,
            "r": None,
            "s": None,
            "t": None,
            "u": None,
            "v": None,
            "w": None,
            "x": None,
            "y": None,
            "z": None,
        }

    def get_leaves(self) -> dict:
        return self.leaves

    def append_word(self, word: str):
        self.words.append(word)

    def get_words(self) -> list:
        return self.words


class PrefixTree:
    def __init__(self, words: list = None):
        self.root = Node()
        if words is not None:
            for word in words:
                self.add_word(word)

    def add_word(self, word: str, rep: str = None):
        node = self.root
        rep = word if rep is None else rep
        i = 0
        for c in word:
            leaves = node.get_leaves()
            if leaves[c] is None:
                leaves[c] = Node()
            node = leaves[c]
            i += 1
            if i == len(word):
                node.append_word(rep)

    def get_matches(self, word: str) -> list:
        word = sorted(word)
        node = self.root
        for c in word:
            leaves = node.get_leaves()
            if leaves[c] is None:
                return []
            node = leaves[c]
        return node.get_words()


class SortedPrefixTree(PrefixTree):
    def add_word(self, word: str):
        super().add_word(''.join(sorted(word)), word)
