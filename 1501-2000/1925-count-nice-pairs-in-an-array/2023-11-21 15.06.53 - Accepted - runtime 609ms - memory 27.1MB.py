class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        # {i:(v-self.reversed(v)) for i,v in enumerate(nums)}

        MOD = 10**9 + 7

        # Calculate the count of nice pairs
        count = 0
        reverse_counts = {}

        for n in nums:
            diff = n-self.reversed(n)

            # Increment count based on the difference
            count += reverse_counts.get(diff, 0)
            count %= MOD

            # print(count,diff)

            # Update the reverse_counts dictionary
            reverse_counts[diff] = reverse_counts.get(diff, 0) + 1

        # print(reverse_counts)

        return count

    def reversed(self, x):
        return int(str(x)[::-1])