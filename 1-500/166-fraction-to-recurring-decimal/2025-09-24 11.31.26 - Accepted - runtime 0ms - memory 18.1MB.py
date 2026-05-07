class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        
        result = []
        
        # Handle negative sign
        if (numerator > 0) ^ (denominator > 0): result.append('-')
        
        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        
        # Get remainder
        numerator %= denominator
        
        # If no remainder, it's a terminating decimal
        if numerator == 0: return ''.join(result)
        
        # Start decimal part
        result.append('.')
        
        # Track remainders and their positions for cycle detection
        remainder_positions = {}
        
        while numerator != 0:
            # If we've seen this remainder before, we have a cycle
            if numerator in remainder_positions:
                # Insert opening parenthesis at the start of the cycle
                cycle_start = remainder_positions[numerator]
                result.insert(cycle_start, '(')
                result.append(')')
                break
            
            # Record the position of this remainder
            remainder_positions[numerator] = len(result)
            
            # Continue long division
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator
        
        
        return ''.join(result)