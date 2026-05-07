class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        L=len(s)
        res=0
        left=0
        arr01=[0,0]
        
        for right in range(L):
            arr01[s[right]=='1']+=1
            
            # Shrink the window if it violates the constraint
            while arr01[0]>k and arr01[1]>k:
                arr01[s[left]=='1']-=1
                left+=1
            
            # All substrings ending at 'right' and starting from 'left' to 'right' are valid
            res+=(right-left+1)
        

        return res