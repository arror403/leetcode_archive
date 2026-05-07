class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word2 = word[0].lower()+word[1:]
        return (word == word.upper()) or (word == word.lower()) or (word.lower() == word2)