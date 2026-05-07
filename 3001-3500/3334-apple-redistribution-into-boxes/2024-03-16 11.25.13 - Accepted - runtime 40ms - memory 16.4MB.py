class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return next(i+1 for i,v in enumerate(accumulate(sorted(c,reverse=1))) if v>=sum(a))

        # print(s,sorted(capacity, reverse=True))
        # res=0
        # for i in sorted(capacity, reverse=True):
        #     if s-i>=0:
        #         res+=1
        #         s-=i
        # return res