class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Sort the array in ascending order
        arr.sort()
        
        # Calculate the common difference between consecutive elements
        diff = arr[1] - arr[0]
        
        # Check if the remaining elements have the same difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True