class Solution:
    def countTestedDevices(self, b: List[int]) -> int:
        count=0
        for i in range(len(b)):
            if b[i]>count:
                count+=1

        return count