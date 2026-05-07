class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        char_index = {}
        for i, c in enumerate(s):
            if c not in char_index:
                char_index[c] = i
            else:
                max_len = max(max_len, i - char_index[c] - 1)
        return max_len