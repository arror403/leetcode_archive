class Solution:
    def punishmentNumber(self, n: int) -> int:
        res=0

        for i in range(1, n+1):
            qi=i**2
            qs=str(qi)
            if self.canPartition(qs, 0, i):
                res+=qi

        return res


    def canPartition(self, s, startIdx, target):
        if (startIdx==len(s) and target==0): return True
        if target<0: return False
        
        ans=False
        leftNum=0

        for i in range(startIdx, len(s)):
            leftNum=leftNum*10+int(s[i])
            isPossible=self.canPartition(s, i+1, target-leftNum)
            if isPossible:
                ans=True
                break

        return ans