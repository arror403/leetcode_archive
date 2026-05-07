class Solution:
    ##### improved by Claude #####
    def numberOfSpecialChars(self, word: str) -> int:
        char_indices = defaultdict(list)
        for i, c in enumerate(word):
            char_indices[c].append(i)

        result = 0
        for c in set(c for c in word if c.islower()):
            upper_c = c.upper()
            if upper_c in char_indices:
                upper_indices = char_indices[upper_c]
                lower_indices = char_indices[c]
                if all(i < upper_indices[0] for i in lower_indices):
                    result += 1

        return result