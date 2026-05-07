class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p,q=set(),set()

        for n in map(str,arr1):
            for i in range(len(n)):
                if (t:=n[:i+1]) not in p: p.add(t)

        for n in map(str,arr2):
            for i in range(len(n)):
                if (t:=n[:i+1]) not in q: q.add(t)


        return len(max(p&q, key=len, default=''))