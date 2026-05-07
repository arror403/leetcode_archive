class Solution:

    ##### power by chatGPT #####

    def minimumLength(self, s: str) -> int:
        left,right=0,len(s)-1

        while left<right and s[left]==s[right]:
            # Keep moving pointers inward if characters are equal
            char=s[left]
            while left<=right and s[left]==char:
                left+=1
            while right>=left and s[right]==char:
                right-=1

        return max(right-left+1, 0)