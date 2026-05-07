class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []  # Initialize an empty list to store the operations
        index = 1    # Initialize the current number to 1
        
        for t in target:
            # While the current number is less than the target, keep pushing and incrementing.
            while index < t:
                result.append("Push")
                result.append("Pop")
                index += 1
            
            result.append("Push")  # Push the target element
            index += 1
        
        return result