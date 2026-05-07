class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to 0-indexed
            remainder = columnNumber % 26
            res.append(chr(65 + remainder))  # Convert to corresponding character
            columnNumber //= 26
        
        res.reverse()
        
        return ''.join(res)