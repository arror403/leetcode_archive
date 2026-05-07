class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t=ord(target)

        for c in letters:
            if ord(c)>t:
                return c

        return letters[0]