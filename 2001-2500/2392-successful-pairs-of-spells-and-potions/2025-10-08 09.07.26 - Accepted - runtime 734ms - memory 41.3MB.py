class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = [0] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            l = 0
            r = m - 1
            while l <= r:
                mid = l + (r - l) // 2
                product = spell * potions[mid]

                if product >= success:
                    r = mid - 1
                else:
                    l = mid + 1

            pairs[i] = m - l


        return pairs