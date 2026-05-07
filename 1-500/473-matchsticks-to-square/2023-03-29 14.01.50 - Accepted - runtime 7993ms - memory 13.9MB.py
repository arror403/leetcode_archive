class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        sides = [0] * 4
        return self.dfs(matchsticks, sides, target, 0)
        
    def dfs(self, matchsticks, sides, target, index):
        if index == len(matchsticks):
            return all(side == target for side in sides)
        for i in range(4):
            if sides[i] + matchsticks[index] > target:
                continue
            sides[i] += matchsticks[index]
            if self.dfs(matchsticks, sides, target, index + 1):
                return True
            sides[i] -= matchsticks[index]
        return False