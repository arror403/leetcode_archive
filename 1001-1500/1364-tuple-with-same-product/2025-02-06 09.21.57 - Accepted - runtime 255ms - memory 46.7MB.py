class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # d=Counter([a*b for a,b in combinations(nums,2)])
        # print(d)

        return sum(v*(v-1)*4 for v in Counter(a*b for a,b in combinations(nums,2)).values() if v>1)