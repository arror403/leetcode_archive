class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s)==len(set(s)): return -1
        
        index_dict = {}
        max_dist = -1

        for i, v in enumerate(s):
            if v in index_dict:
                max_dist = max(max_dist, i - index_dict[v])
            else:
                index_dict[v] = i

        return max_dist-1