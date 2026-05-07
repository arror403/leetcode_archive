class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        cumulative_sum = 0
        for i, digit in enumerate(word):
            cumulative_sum = (cumulative_sum * 10 + int(digit)) % m
            if cumulative_sum == 0:
                res.append(1)
            else:
                res.append(0)
        return res