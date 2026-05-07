class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def search(self, word):
        return self._search_helper(word, self.root)
        
    def _search_helper(self, word, node):
        if not word:
            return node.is_word
        
        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self._search_helper(word[1:], child):
                    return True
        elif char in node.children:
            return self._search_helper(word[1:], node.children[char])
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)