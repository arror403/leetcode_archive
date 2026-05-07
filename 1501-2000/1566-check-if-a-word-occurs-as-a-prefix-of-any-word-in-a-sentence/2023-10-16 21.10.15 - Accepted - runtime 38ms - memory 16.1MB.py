class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        return next((i+1 for i,v in enumerate(sentence.split()) if v.startswith(searchWord)), -1)