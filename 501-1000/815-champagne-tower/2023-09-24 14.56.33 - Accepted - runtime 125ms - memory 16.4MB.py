class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create a 2D list to represent the champagne glasses
        glasses = [[0] * (i + 1) for i in range(query_row + 1)]
        
        # Initialize the top glass with the poured amount
        glasses[0][0] = poured
        
        # Traverse each row and calculate the overflow for each glass
        for row in range(query_row):
            for col in range(len(glasses[row])):
                overflow = max(0, glasses[row][col] - 1) / 2.0
                glasses[row + 1][col] += overflow
                glasses[row + 1][col + 1] += overflow
        
        # Ensure the value is between 0 and 1 (no more than one glass can hold)
        return min(1, glasses[query_row][query_glass])



        # if poured>=5050: return 1

        # res=[[] for _ in range(100)]

        # for i in range(100):
        #     if poured>=(i+1):
        #         poured-=(i+1)
        #         res[i]+=[1 for _ in range(i+1)]
        #     else:
        #         res[i]+=[poured*(math.comb(i,j)/2**i) for j in range(i+1)]
        #         break

        # for i in range(100):
        #     if not res[i]: # if is empty
        #         res[i]+=[0 for _ in range(i+1)]

        # return res[query_row][query_glass]