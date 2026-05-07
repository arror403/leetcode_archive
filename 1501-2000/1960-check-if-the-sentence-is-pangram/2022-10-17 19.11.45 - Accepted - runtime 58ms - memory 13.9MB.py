class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(dict.fromkeys(list(sentence)))==26