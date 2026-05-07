class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        # Pre-compute absolute differences to avoid redundant calculations
        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i] - arr[j]) <= a:  # Only proceed if first condition is met
                    for k in range(j+1, n):
                        # Check remaining conditions only when needed
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        
        return count