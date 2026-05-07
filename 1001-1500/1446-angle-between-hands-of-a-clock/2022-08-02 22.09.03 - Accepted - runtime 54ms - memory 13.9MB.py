class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        return min(abs((hour%12)*30-minutes*5.5),360-abs((hour%12)*30-minutes*5.5))