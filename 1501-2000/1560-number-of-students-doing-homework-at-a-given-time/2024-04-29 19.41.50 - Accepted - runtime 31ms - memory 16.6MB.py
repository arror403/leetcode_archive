class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(1 for a,b in zip(startTime,endTime) if (queryTime>=a and queryTime<=b))