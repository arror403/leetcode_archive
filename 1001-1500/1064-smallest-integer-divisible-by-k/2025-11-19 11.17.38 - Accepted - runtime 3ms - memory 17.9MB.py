class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0: return -1

        remainder = 0
        
        # Optimization 2: Only iterate up to K.
        # By the Pigeonhole Principle, if we don't find a remainder of 0 
        # within K iterations, the remainders will start repeating in a cycle 
        # that never hits 0.
        for length in range(1, k + 1):
            # Optimization 3: Keep numbers small.
            # We update the remainder directly without string conversion.
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length


        return -1

        # sys.set_int_max_str_digits(100000)
        # res='1'

        # for _ in range(10000):
        #     if int(res)%k==0: return len(res)

        #     res+='1'

        # return -1