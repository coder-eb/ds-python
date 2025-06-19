class MonotonicQueue:
    def __init__(self):
        self.maxq = []

    def max(self):
        if len(self.maxq) == 0:
            return None
        return self.maxq[0]

    def push(self, n: int):
        while len(self.maxq) > 0 and self.maxq[-1] < n:
            self.maxq.pop()

        self.maxq.append(n)

    def pop(self, n: int) -> int:
        if len(self.maxq) == 0:
            return None
        
        if self.maxq[0] == n:
            self.maxq.pop(0)

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                curr_node.children[position] = TrieNode()
            
            curr_node = curr_node.children[position]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
        return True

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.min_stack) > 0:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def test_trie():
    trie = Trie()
    trie.insert('apple')
    print(trie.search('applee'))
    print(trie.startsWith('apple'))

def main():
    test_trie()

if __name__ == '__main__':
    main()
