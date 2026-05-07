class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = ''.join(sorted(tiles))
        fact = [1, 1, 2, 6, 24, 120, 720, 5040]
        st = set()
        
        def uniquePerms(s):
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - 65] += 1
            res = fact[len(s)]
            for n in cnt:
                if n > 0:  # Only divide by factorial if count > 0
                    res //= fact[n]
            return res
        
        def dfs(s, seq, pos):
            if pos >= len(s):
                if seq not in st:
                    st.add(seq)
                    return uniquePerms(seq)
                return 0
            
            return dfs(s, seq, pos+1) + dfs(s, seq+s[pos], pos+1)
        

        return dfs(tiles, "", 0) - 1