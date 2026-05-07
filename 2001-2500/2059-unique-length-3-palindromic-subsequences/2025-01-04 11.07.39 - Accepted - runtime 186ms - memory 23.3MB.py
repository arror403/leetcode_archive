class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # p=list(combinations([chr(i) for i in range(97, 123)], 2))
        d=Counter(s)
        m=defaultdict(list)
        res=0

        for i,c in enumerate(s): m[c].append(i)

        for v in d.values():
            if v>=3: res+=1

        for i in range(97, 123):
            c1 = chr(i)
            if c1 not in m: 
                continue

            for j in range(97, 123):
                c2 = chr(j)
                if c2 == c1 or c2 not in m:
                    continue
                # Check if there's c2 between first and last occurrence of c1
                if d[c1]>=2:
                    # Check if any c2 exists between first and last c1
                    for idx in m[c2]:
                        if m[c1][0] < idx < m[c1][-1]:
                            res += 1
                            break
        
        # for x in p:
        #     i,j=x[0],x[1]
        #     if (d[i]>=2 and d[j]>=1) and (m[i][-1]>m[j][-1]):
        #         res+=1
        #     if (d[i]>=1 and d[j]>=2) and (m[i][-1]<m[j][-1]):
        #         res+=1

        return res