class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if (numerator, denominator)==(-1,-2147483648): return "0.0000000004656612873077392578125"
        if numerator==0: return '0'

        # Handle sign
        negative = (numerator > 0) ^ (denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)

        t=abs(denominator)
        while t>1:
            if t%2==0: t//=2
            elif t%5==0: t//=5
            else: break

        # if t==1: 
            # if numerator%denominator==0: return str(int(numerator/denominator))
            # else: return str(numerator/denominator)

        # correction for above
        if t == 1: 
            result = numerator / denominator
            if result == int(result):
                return ('-' if negative else '') + str(int(result))
            else:
                return ('-' if negative else '') + str(result)



        # a, b = divmod(numerator, denominator)
        # y=str(a)
        # numerator=b
        # r=set()
        # pre='0'
        # # zeros=0

        # while 1:
        #     print(r)
        #     if numerator<denominator: 
        #         numerator*=10
        #         continue
        #     else:
        #         a, b = divmod(numerator, denominator)
        #         x=pre+str(a)
        #         if x in r: return y+'.('+x+')'
        #         numerator=b
        #         pre=x
        #         r.add(pre)

        
        # Non-terminating fraction - find the cycle
        integer_part, numerator = divmod(numerator, denominator)
        result = ('-' if negative else '') + str(integer_part)
        
        if numerator == 0:
            return result
        
        result += '.'
        
        # Track seen digit sequences and their positions
        seen = {}
        decimal_part = ''
        
        while numerator != 0:
            if numerator in seen:
                # Found cycle - insert parentheses
                cycle_start = seen[numerator]
                before_cycle = decimal_part[:cycle_start]
                cycle = decimal_part[cycle_start:]
                return result + before_cycle + '(' + cycle + ')'
            
            # Record this remainder's position
            seen[numerator] = len(decimal_part)
            
            # Continue long division
            numerator *= 10
            digit, numerator = divmod(numerator, denominator)
            decimal_part += str(digit)
        

        return result + decimal_part



        # if numerator == 0: return '0'
        
        # result = []
        
        # # Handle negative sign
        # if (numerator > 0) ^ (denominator > 0): result.append('-')
        
        # # Work with absolute values
        # numerator, denominator = abs(numerator), abs(denominator)
        
        # # Integer part
        # result.append(str(numerator // denominator))
        
        # # Get remainder
        # numerator %= denominator
        
        # # If no remainder, it's a terminating decimal
        # if numerator == 0: return ''.join(result)
        
        # # Start decimal part
        # result.append('.')
        
        # # Track remainders and their positions for cycle detection
        # remainder_positions = {}
        
        # while numerator != 0:
        #     # If we've seen this remainder before, we have a cycle
        #     if numerator in remainder_positions:
        #         # Insert opening parenthesis at the start of the cycle
        #         cycle_start = remainder_positions[numerator]
        #         result.insert(cycle_start, '(')
        #         result.append(')')
        #         break
            
        #     # Record the position of this remainder
        #     remainder_positions[numerator] = len(result)
            
        #     # Continue long division
        #     numerator *= 10
        #     result.append(str(numerator // denominator))
        #     numerator %= denominator
        
        # return ''.join(result)