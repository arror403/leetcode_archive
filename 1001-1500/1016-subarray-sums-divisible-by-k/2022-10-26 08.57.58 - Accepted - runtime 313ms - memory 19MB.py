class Solution:
    def subarraysDivByK(self, nums: List[int], t: int) -> int:
        # Handles all the cases
        # function to find all
        # sub-arrays divisible by k
        # modified to handle
        # negative numbers as well
        def subCount(arr, k):
            n=len(arr)
            # create auxiliary hash
            # array to count frequency
            # of remainders
            mod =[]
            for i in range(k + 1):
                mod.append(0)
        
            # Traverse original array
            # and compute cumulative
            # sum take remainder of this
            # current cumulative
            # sum and increase count by
            # 1 for this remainder
            # in mod[] array
            cumSum = 0
            for i in range(n):
                cumSum = cumSum + arr[i]
                
                # as the sum can be negative,
                # taking modulo twice
                mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
            
        
            result = 0  # Initialize result
            
            # Traverse mod[]
            for i in range(k):
        
                # If there are more than
                # one prefix subarrays
                # with a particular mod value.
                if (mod[i] > 1):
                    result = result + (mod[i]*(mod[i]-1))//2
            
            # add the elements which
            # are divisible by k itself
            # i.e., the elements whose sum = 0
            result = result + mod[0]
            
            return result
        return subCount(nums,t)