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
        self.terminal = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr_node = self.root
        for i, letter in enumerate(word):
            terminal = (i == len(word)-1)
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                curr_node.children[position] = TrieNode()
            
            curr_node = curr_node.children[position]
            if terminal:
                curr_node.terminal = terminal

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i, letter in enumerate(word):
            terminal = (i == len(word)-1)
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
            if terminal and curr_node.terminal:
                return True 
        return False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for i, letter in enumerate(prefix):
            position = ord(letter)-ord('a')
            if not curr_node.children[position]:
                return False
            
            curr_node = curr_node.children[position]
        return True
     
def test_trie():
    trie = Trie()
    trie.insert('apple')
    print(trie.search('applee'))
    print(trie.startsWith('apple'))

def main():
    test_trie()

if __name__ == '__main__':
    main()

