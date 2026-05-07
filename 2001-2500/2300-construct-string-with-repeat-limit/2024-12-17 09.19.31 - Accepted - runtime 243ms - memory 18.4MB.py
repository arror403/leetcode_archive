class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d = Counter(s)
        chars = sorted(d.keys(), reverse=True)
        res = ""
        i = 0

        while i < len(chars):
            curr_char = chars[i]
            
            if d[curr_char] > repeatLimit:
                res += curr_char * repeatLimit
                d[curr_char] -= repeatLimit
                # Try to find a different character to break the sequence
                found_break = False
                for j in range(i + 1, len(chars)):
                    if d[chars[j]] > 0:
                        res += chars[j]
                        d[chars[j]] -= 1
                        found_break = True
                        break
                # If no break character found, we're done
                if found_break==False:
                    break
            else:
                # Add all remaining occurrences of the current character
                res += curr_char * d[curr_char]
                d[curr_char] = 0
                i += 1
        

        return res