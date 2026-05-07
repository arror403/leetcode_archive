class Solution:
    def greatestLetter(self, s: str) -> str:
        return max((chr(65+i) for i in range(26) if chr(97+i) in s and chr(65+i) in s), default="")
