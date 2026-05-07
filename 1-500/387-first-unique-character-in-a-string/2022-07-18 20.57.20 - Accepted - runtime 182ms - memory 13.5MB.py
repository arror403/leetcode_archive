class Solution:
    def firstUniqChar(self, s: str) -> int:
        # s=list(s)
        # f=1
        # for i in s:
        #     if s.count(i)==1:
        #         f=0
        #         return s.index(i)
        #         break
        # if f: return -1
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1