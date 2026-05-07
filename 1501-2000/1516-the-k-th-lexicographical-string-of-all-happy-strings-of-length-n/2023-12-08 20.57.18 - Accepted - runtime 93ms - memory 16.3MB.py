class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ##### power by chatGPT #####
        def backtrack(s):
            nonlocal count, result
            if len(s) == n:
                count += 1
                if count == k:
                    result = s
                return
            for char in "abc":
                if not s or s[-1] != char:
                    backtrack(s + char)

        count = 0
        result = ""
        backtrack("")
        return result