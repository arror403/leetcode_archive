class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d=deque(map(bool,nums))
        res=0

        while len(d)>3:
            if not d[0]:
                d[1]=not d[1]
                d[2]=not d[2]
                res+=1
            
            d.popleft()
            # print(d)

        s=set(d)
        if len(s)==1:
            if s.pop(): return res
            else: return res+1

        return -1