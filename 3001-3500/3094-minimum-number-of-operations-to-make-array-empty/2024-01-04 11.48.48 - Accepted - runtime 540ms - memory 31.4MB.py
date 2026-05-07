class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0

        for x in Counter(nums).values():
            if self.min_sum(x)==None: return -1
            else: res+=self.min_sum(x)

        return res

    def min_sum(self, n):
        x=n//3
        while x>=0:
            if (n-3*x)%2==0:
                y=(n-3*x)//2
                return x+y
            x-=1
        return None