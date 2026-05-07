class Solution:
    def findIndices(self, nums: List[int], Di: int, Dv: int) -> List[int]:
        for i,v1 in enumerate(nums):
            for j,v2 in enumerate(nums):
                if abs(i-j)>=Di and abs(v1-v2)>=Dv:
                    return [i,j]
        return [-1,-1]


        # if nums==[0]: return [-1,-1]

        # t=[[i[0],j[0]] for i,j in combinations([[i,v] for i,v in enumerate(nums)],2) if (abs(i[0]-j[0])>=Di and abs(i[1]-j[1])>=Dv)]

        # return t[0] if t else [-1,-1]