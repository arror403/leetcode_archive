class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # res=set()

        # for i in nums:
        #     res = res | {x for x in range(i[0],i[1]+1)}

        # return len(res)
        return len(set(x for i in nums for x in range(i[0], i[1]+1)))