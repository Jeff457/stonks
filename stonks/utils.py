from collections import deque


class Trie:
    TERMINAL = "#"

    def __init__(self, words: list):
        self.root = {}
        self._build(words)

    def _build(self, words: list):
        for word in words:
            node = self.root
            for char in word.lower():
                node = node.setdefault(char, {})
            node[self.TERMINAL] = word

    def search(self, sentence: str):
        queue = deque([self.root])

        i = 0
        while i < len(sentence):
            if not queue:
                queue.append(self.root)
            for _ in range(len(queue)):
                node = queue.popleft()
                char = sentence[i]
                if char in node:
                    queue.append(node[char])
                    if self.TERMINAL in node[char]:
                        # TODO: probably want to accumulate a set of matches
                        return node[char][self.TERMINAL].upper()

            i += 1

        return None
