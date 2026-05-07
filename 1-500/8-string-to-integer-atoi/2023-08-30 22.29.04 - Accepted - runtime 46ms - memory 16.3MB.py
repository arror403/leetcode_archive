class Solution:
    def myAtoi(self, s: str) -> int:
        t = []
        is_negative = False
        is_sign_found = False
        
        for i in s:
            if i == ' ':
                if not t and not is_sign_found:
                    continue
                else:
                    break
            elif i == '-' or i == '+':
                if not t and not is_sign_found:
                    is_sign_found = True
                    is_negative = (i == '-')
                else:
                    break
            elif i.isnumeric():
                t.append(i)
            else:
                break
        
        t = ''.join(t)
        if len(t) == 0:
            return 0
        
        result = 0
        for digit in t:
            result = result * 10 + int(digit)
        
        if is_negative:
            result = -result
        
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        
        return result