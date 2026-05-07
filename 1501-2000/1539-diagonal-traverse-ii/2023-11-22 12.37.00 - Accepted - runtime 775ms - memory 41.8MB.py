class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        # print(d)

        # d = defaultdict(list,{k:[nums[i][j] for i in range(len(nums)) for j in range(len(nums[i])) if i+j==k] for k in range(len(nums)*2-1)})


        return [i for v in d.values() for i in v[::-1]]