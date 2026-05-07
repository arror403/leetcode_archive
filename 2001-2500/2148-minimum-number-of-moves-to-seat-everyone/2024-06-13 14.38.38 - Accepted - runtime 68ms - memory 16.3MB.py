class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum((x-y) if x>=y else (y-x) for x,y in zip(sorted(seats),sorted(students)))