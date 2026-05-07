class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(num):
            c=0
            while num:
                c+=1
                num&=(num-1)

            return c

        return sorted(arr, key=lambda x:(countBits(x), x))