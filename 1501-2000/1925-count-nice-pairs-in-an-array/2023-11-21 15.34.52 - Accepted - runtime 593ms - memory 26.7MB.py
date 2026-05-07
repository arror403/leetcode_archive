class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        count = 0
        reverse_counts = {}

        for n in nums:
            diff = n-self.reversed(n)

            tmp=reverse_counts.get(diff, 0)

            count += tmp

            # print(count,diff)

            reverse_counts[diff] = tmp+1

        # print(reverse_counts)

        return count%(10**9+7)



    def reversed(self, x):
        return int(str(x)[::-1])