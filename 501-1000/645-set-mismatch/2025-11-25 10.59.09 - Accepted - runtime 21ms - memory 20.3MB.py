class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        r = range(1, len(nums)+1)
        res = []

        for v in r:
            if d[v]>1:
                res.append(v)
                break

        res += list(set(r) - set(nums))


        return res