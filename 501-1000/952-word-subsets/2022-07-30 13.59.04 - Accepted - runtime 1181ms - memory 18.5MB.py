class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
    
#         res=[]
#         words2=''.join(words2)
#         words2=list(set(words2))
#         for i in words1:
#             f=True
#             for j in words2:
#                 if j in i:
#                     continue
#                 else:
#                     f=False
#                     break
                    
#             if f: 
#                 # i=''.join(i)
#                 res.append(i)
                
#         return res