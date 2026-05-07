class Solution:
    def knightDialer(self, N: int) -> int:
        # Define the valid moves for the knight
        moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        @lru_cache(maxsize=None)
        def count_ways(position, steps_left):
            if steps_left == 0: return 1

            total_ways = 0
            for neighbor in moves[position]:
                total_ways += count_ways(neighbor, steps_left - 1)

            return total_ways

        # Initialize the count starting from each digit
        
        # total_count = 0
        # for i in range(10):
        #     total_count += count_ways(i, N-1)

        # return total_count 

        return sum([count_ways(i, N-1) for i in range(10)])%(10**9+7)