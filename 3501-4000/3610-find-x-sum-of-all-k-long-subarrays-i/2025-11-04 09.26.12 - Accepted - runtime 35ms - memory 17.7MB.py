class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = Counter(nums[:k])
        L = len(nums)
        res = []

        for i in range(L-k+1):
            res.append(sum(y*d[y] for y in nlargest(x, d, key=lambda x: (d[x], x))))
            d[nums[i]] -= 1
            if (i+k) < L:
                d[nums[i+k]] += 1


        return res