class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start=bin(start)[2:]
        goal=bin(goal)[2:]
        res=0
        a,b=len(start),len(goal)
        if a>b:
            x = '0'*(a-b)
            goal=x+goal
        else:
            x = '0'*(b-a)
            start=x+start

        for i in range(max(a,b)):
            if start[i]!=goal[i]:
                res+=1

        return res