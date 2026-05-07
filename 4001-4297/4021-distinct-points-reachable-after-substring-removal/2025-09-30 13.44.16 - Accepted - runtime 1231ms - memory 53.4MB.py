class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n=len(s)
        d={'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
        pre=[[0,0] for _ in range(n+1)]
        suf=[[0,0] for _ in range(n+1)]

        for i in range(n):
            pre[i+1][0]=pre[i][0]
            pre[i+1][1]=pre[i][1]
            pre[i+1][0]+=d[s[i]][0]
            pre[i+1][1]+=d[s[i]][1]

        # c=[0,0]
        # for x in s[::-1]:
        #     c[0]-=d[x][0]
        #     c[1]-=d[x][1]
        #     suf.append(c)
        for i in range(n-1,-1,-1):
            suf[i][0]=suf[i+1][0]
            suf[i][1]=suf[i+1][1]
            suf[i][0]+=d[s[i]][0]
            suf[i][1]+=d[s[i]][1]

        S=set()
        for i in range(n-k+1): S.add((pre[i][0]+suf[i+k][0], pre[i][1]+suf[i+k][1]))

        # print(S)
        return len(S)


        # for i in range(len(s)-k):
        #     # print(s[:i]+s[i+k:])

        # for x in s[:k]:
        #     c[0]+=d[x][0]
        #     c[1]+=d[x][1]

        # for i in range(L-k+1):
        #     c[0]-=d[s[L-1-i]][0]
        #     c[1]-=d[s[L-1-i]][1]
        #     c[0]+=d[s[k+i]][0]
        #     c[1]+=d[s[k+i]][1]
        #     if tuple(c) not in S: S.add(tuple(c))