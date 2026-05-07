class Solution:
    def countSubstrings(self, s: str) -> int:

        ##### power by chatGPT #####

        count = 0

        def expand_around_center(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_center(i, i)  # for odd-length palindromes
            expand_around_center(i, i + 1)  # for even-length palindromes

        return count