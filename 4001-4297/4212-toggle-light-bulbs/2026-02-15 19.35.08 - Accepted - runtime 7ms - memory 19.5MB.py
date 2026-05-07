class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        return sorted([v for v,f in Counter(bulbs).items() if f%2])