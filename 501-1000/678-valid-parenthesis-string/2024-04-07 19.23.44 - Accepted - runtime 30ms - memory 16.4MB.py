class Solution:
    ##### power by chatGPT #####
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:  # char == '*'
                if low > 0:
                    low -= 1
                high += 1
            
            # If high becomes negative, it means there are more ')' than '(' and '*'
            if high < 0:
                return False
        
        # If low is not zero at the end, it means there are more '(' than ')'
        return low == 0
