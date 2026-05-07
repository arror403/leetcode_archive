class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 1

        # left border of the window
        for left in range(n):
            freq = defaultdict(int)      # frequency of characters in the current window
            distinct = 0                 # number of different characters inside the window
            minFreq = 0                  # minimum frequency among the characters that appear
            maxFreq = 0                  # maximum frequency among the characters that appear

            # right border of the window – expand the window
            for right in range(left, n):
                ch = s[right]

                if freq[ch] == 0:
                    distinct += 1
                freq[ch] += 1

                minFreq = min(freq.values())
                maxFreq = max(freq.values())

                if maxFreq == minFreq:
                    max_len = max(max_len, right - left + 1)


        return max_len