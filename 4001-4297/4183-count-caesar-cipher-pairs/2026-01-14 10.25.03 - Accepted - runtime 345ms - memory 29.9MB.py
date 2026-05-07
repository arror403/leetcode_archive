class Solution:
    def countPairs(self, words: List[str]) -> int:
        L = len(words[0])
        m = defaultdict(int)
        res = 0

        for w in words:
            normalized = [0] * L
            shift = ord(w[0]) - 97

            for i in range(L):
                normalized[i] = chr(97 + (ord(w[i]) - 97 - shift + 26) % 26)
                
            k = ''.join(normalized)
            res += m[k]
            m[k] += 1
        
        
        return res