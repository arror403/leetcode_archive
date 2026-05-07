class Solution:
    def clearStars(self, s: str) -> str:
        pq = []  # min heap
        indices = [[] for i in range(26)]
        removeSet = set()
        res = ""
        
        for i in range(len(s)):
            if s[i] == '*':
                removeSet.add(i)
                ch = heappop(pq)
                heappush(pq, ch)
                removeSet.add(indices[ord(ch) - ord('a')][-1])
                del indices[ord(ch) - ord('a')][-1]
                if len(indices[ord(ch) - ord('a')]) == 0:
                    heappop(pq)
                continue
            
            if len(indices[ord(s[i]) - ord('a')]) == 0:
                heappush(pq, s[i])
            indices[ord(s[i]) - ord('a')].append(i)
        
        for i in range(len(s)):
            if i not in removeSet:
                res += s[i]
        
        return res