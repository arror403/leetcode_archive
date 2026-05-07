class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            # print(i)
            if int(num[i])%2==0: continue
            return num[0:i+1]
                
        return ""