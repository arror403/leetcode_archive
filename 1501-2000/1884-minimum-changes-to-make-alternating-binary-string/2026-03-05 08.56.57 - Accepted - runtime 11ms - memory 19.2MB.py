class Solution:
    def minOperations(self, s: str) -> int:
        a=b=0

        for i in range(len(s)):
            if (i%2)==0: 
                if s[i]=='0':
                    b+=1
                else:
                    a+=1
            else: # i%2 == 1
                if s[i]=='1':
                    b+=1
                else:
                    a+=1


        return min(a, b)