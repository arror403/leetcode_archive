class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l_p = len(p)
        l_s = len(s)
        
        # Initialize Counters for pattern and the first substring in s
        p_counter = Counter(p)
        s_counter = Counter(s[:l_p])
        
        res = []

        # Check the first substring
        if s_counter == p_counter:
            res.append(0)

        # Iterate through the rest of the substrings using a sliding window
        for i in range(1, l_s - l_p + 1):
            # Update the sliding window Counter
            s_counter[s[i - 1]] -= 1
            if s_counter[s[i - 1]] == 0:
                del s_counter[s[i - 1]]
            
            s_counter[s[i + l_p - 1]] += 1

            # Check if the current substring is an anagram
            if s_counter == p_counter:
                res.append(i)

        return res