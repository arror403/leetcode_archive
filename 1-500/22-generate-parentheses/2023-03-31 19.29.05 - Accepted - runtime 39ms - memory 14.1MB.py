class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, "", 0, 0, res)
        return res
    
    def backtrack(self, n, curr, left, right, res):
        if len(curr) == n * 2:
            res.append(curr)
            return
        
        if left < n:
            self.backtrack(n, curr + "(", left + 1, right, res)
        
        if right < left:
            self.backtrack(n, curr + ")", left, right + 1, res)