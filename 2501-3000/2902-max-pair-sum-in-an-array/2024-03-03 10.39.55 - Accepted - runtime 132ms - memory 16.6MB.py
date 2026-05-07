class Solution:
    ##### improved by chatGPT #####
    def max_digit(self, n):
        """Function to find the maximum digit in a number."""
        digits = map(int, str(n))
        return max(digits)

    def maxSum(self, nums: List[int]) -> int:
        """
        Function to find the maximum sum of the two largest numbers
        in groups based on the maximum digit in each number.
        """
        # Step 1: Sort the numbers based on their maximum digits.
        m = sorted([[v, self.max_digit(v)] for v in nums], key=lambda x:x[1])
        
        # Step 2: Group the numbers based on their maximum digits.
        groups = [list(g) for _,g in groupby(m, key=lambda x:x[1])]
        
        # Step 3: Calculate the maximum sum of the two largest numbers in each group.
        max_sum = max([sum(nlargest(2, [x[0] for x in i])) for i in groups if len(i)>1], default=-1)

        return max_sum