class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i+j].append(nums[i][j])
        result = []
        # for key, values in diagonals.items():
        #     if key % 2 == 0:
        #         result.extend(values[::-1])
        #     else:
        #         result.extend(values)

        for v in diagonals.values():
            result.extend(v[::-1])


        return result