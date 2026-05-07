class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        mismatch=0
        
        for i in range(len(s)):
            ch=s[i]

            if ch=='[':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    mismatch+=1


        return (mismatch+1)//2