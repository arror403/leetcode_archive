class Solution:
    def maximumLength(self, st: str) -> int:
        mps = defaultdict(int)
        count = 0
        
        for i in range(len(st)):
            count = 1
            mps[(st[i], count)] += 1

            for j in range(i, len(st)):
                if j + 1 < len(st) and st[j] == st[j + 1]:
                    count += 1
                    mps[(st[i], count)] += 1
                else:
                    break
        
        ans1 = 0
        for key, value in mps.items():
            if value >= 3:
                ans1 = max(ans1, key[1])
        
        
        return ans1 if ans1 != 0 else -1