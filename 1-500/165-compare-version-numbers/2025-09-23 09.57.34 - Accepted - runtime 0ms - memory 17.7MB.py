class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        L1, L2 = len(v1), len(v2)
        L = max(L1, L2)

        if L1 < L2: v1 += [0]*(L-L1)
        if L1 > L2: v2 += [0]*(L-L2)

        for a, b in zip(v1, v2):
            a, b = int(a), int(b)
    
            if a > b: return 1
            elif a < b: return -1


        return 0