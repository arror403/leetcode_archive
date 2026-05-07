class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        # Preprocess the string to handle even-length palindromes
        processed_str = '#'.join('^{}$'.format(s))

        n = len(processed_str)
        p = [0] * n  # Array to store the palindrome lengths

        center, right = 0, 0
        max_length, max_center = 0, 0

        for i in range(1, n - 1):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])

            # Attempt to expand the palindrome centered at i
            while processed_str[i + p[i] + 1] == processed_str[i - p[i] - 1]:
                p[i] += 1

            # If palindrome centered at i expands past right boundary, adjust center and right
            if i + p[i] > right:
                center, right = i, i + p[i]

            # Update the maximum palindrome length and its center if necessary
            if p[i] > max_length:
                max_length, max_center = p[i], i

        # Extract the longest palindrome from the processed string
        start = (max_center - max_length) // 2
        end = start + max_length

        return s[start:end]