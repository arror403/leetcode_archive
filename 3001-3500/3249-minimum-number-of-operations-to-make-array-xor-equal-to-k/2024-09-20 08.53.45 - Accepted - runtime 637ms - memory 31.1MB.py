class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        # XOR of all integers in the array.
        finalXor=reduce(lambda x,y:x^y,nums)
        
        # Keep iterating until both k and finalXor becomes zero.
        while (k or finalXor):
            # k % 2 returns the rightmost bit in k,
            # finalXor % 2 returns the rightmost bit in finalXor.
            # Increment counter, if the bits don't match.
            if (k%2)!=(finalXor%2): res+=1
            # Remove the last bit from both integers.
            k//=2
            finalXor//=2


        return res