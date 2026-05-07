class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #start with two largest values, as soon as we find a number bigger than both, while both have been updated, return true
        small = big = inf

        for n in nums:
            if n<=small:
                small=n     #update small if n is smaller than both
            elif n<=big:
                big=n       #update big only if greater than small but smaller than big
            else: 
                return True #return if you find a number bigger than both


        return False