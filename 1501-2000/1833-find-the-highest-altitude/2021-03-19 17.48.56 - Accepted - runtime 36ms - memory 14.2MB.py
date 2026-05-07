class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        b=[0]
        x=0
        for i in range(0,len(gain)):
            b.append(x+gain[i])
            x=x+gain[i]
        return max(b)