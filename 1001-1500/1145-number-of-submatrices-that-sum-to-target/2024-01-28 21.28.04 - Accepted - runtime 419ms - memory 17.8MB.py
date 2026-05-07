class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        ##### power by chatGPT #####

        rows, cols = len(matrix), len(matrix[0])
        # Step 1: Precompute the prefix sum for each row
        for row in matrix:
            for j in range(1, cols):
                row[j] += row[j - 1]

        # Step 2: Iterate through all possible column pairs
        count = 0
        for i in range(cols):
            for j in range(i, cols):
                # Step 3: Create a dictionary to store prefix sum and its count
                prefix_sum = {0: 1}
                cur_sum = 0
                for k in range(rows):
                    # Step 4: Calculate the current sum for submatrix from row 0 to k
                    cur_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    # Step 5: Check if there exists a submatrix with sum equals to target
                    count += prefix_sum.get(cur_sum - target, 0)
                    # Step 6: Update the prefix sum dictionary
                    prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return count


# Explanation:

# 1. Prefix Sum: We precompute the prefix sum for each row. This allows us to compute the sum of any submatrix in O(1) time.
# 2. Iterating through column pairs: We iterate through all possible column pairs (i, j).
# 3. Prefix Sum Dictionary: We maintain a dictionary to store the prefix sum and its count.
# 4. Current Sum Calculation: We calculate the current sum for the submatrix starting from row 0 to row k.
# 5. Counting the Submatrices: We increment the count if there exists a submatrix with sum equals to the target.
# 6. Updating Prefix Sum Dictionary: We update the prefix sum dictionary with the current sum.
# This solution utilizes the concept of prefix sum and dynamic programming to efficiently count the number of submatrices that sum to the target. Make sure to understand each step thoroughly. Feel free to ask if you have any further questions!