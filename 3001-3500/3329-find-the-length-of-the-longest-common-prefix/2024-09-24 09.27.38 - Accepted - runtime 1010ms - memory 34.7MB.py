class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        p,q=set(),set()

        for n in map(str,arr1):
            for i in range(len(n)):
                p.add(n[:i+1])

        for n in map(str,arr2):
            for i in range(len(n)):
                q.add(n[:i+1])


        return len(max(p&q, key=len, default=''))