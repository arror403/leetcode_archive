class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        return bisect_left(range(10**14), cars, key=lambda x: sum(int(sqrt(x/r)) for r in ranks))