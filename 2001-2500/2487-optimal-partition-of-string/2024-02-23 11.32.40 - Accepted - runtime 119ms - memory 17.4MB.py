class Solution:
    def partitionString(self, s: str) -> int:
        m=[0]*26
        res=1

        for i in s:
            if m[ord(i)-97]==1:
                m=[0]*26
                res+=1
                m[ord(i)-97]+=1
            else:
                m[ord(i)-97]+=1

        return res


        # m=[0]*26
        # ans = 0
        # for c in s:
        #     m[ord(c)-97]+=1
        #     if m[ord(c)-97]==1: continue
        #     else:
        #         m=[0]*26
        #         m[ord(c)-97]=1
        #         ans+=1
        # return ans + 1