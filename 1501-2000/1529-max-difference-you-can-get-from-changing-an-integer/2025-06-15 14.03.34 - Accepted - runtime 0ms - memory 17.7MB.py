class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Find maximum value
        max_val = num
        for digit in s:
            if digit != '9':
                # Replace first non-9 digit with 9
                max_val = int(s.replace(digit, '9'))
                break
        
        # Find minimum value
        min_val = num
        if s[0] != '1':
            # If first digit is not 1, replace it with 1
            min_val = int(s.replace(s[0], '1'))
        else:
            # If first digit is 1, find first digit that's not 0 or 1
            for digit in s:
                if digit != '0' and digit != '1':
                    min_val = int(s.replace(digit, '0'))
                    break
        
        
        return max_val - min_val