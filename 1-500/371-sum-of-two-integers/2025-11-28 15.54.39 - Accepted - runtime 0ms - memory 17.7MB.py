class Solution:
    def getSum(self, a: int, b: int) -> int:
        # if a==0: return b
        # if b==0: return a
        # else: return int(log(exp(a) * exp(b)))


        # Mask to get 32-bit representation
        MASK = 0xFFFFFFFF
        # Maximum value for a positive 32-bit signed integer
        MAX_INT = 0x7FFFFFFF
        # Convert both numbers to 32-bit unsigned representation
        a &= MASK
        b &= MASK
        
        # Keep adding until there's no carry left
        while b:
            # Calculate carry bits (AND operation finds where both bits are 1,
            # left shift by 1 to move carry to next position)
            carry = ((a & b) << 1) & MASK
            # XOR gives sum without considering carry
            a = a ^ b
            # Update b to be the carry for next iteration
            b = carry

        # If the result is negative in 32-bit representation,
        # convert back to Python's integer representation
        # Check if MSB (bit 31) is set, indicating negative number
        if a > MAX_INT:
            # Convert from 32-bit two's complement to Python negative integer
            return ~(a ^ MASK)
        else:
            # Positive number, return as is
            return a