class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        L = len(target)
        initial = [0]*L
        res = target[0]

        for i in range(1, L):
            if target[i] > target[i-1]:
                res += target[i] - target[i-1]
        
        
        return res