class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return 0
        if len(s) == 0:
            return 1
        else: 
            subsequence=0
            for i in range(0,len(t)):
                if subsequence <= len(s) -1:
                    # print(s[subsequence])
                    if s[subsequence]==t[i]:
                        subsequence+=1
            return  subsequence == len(s) 