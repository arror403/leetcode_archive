class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        f=defaultdict(int)
        islands=0

        def find(x):
            nonlocal islands
            if f[x]==0:
                f[x]=x
                islands+=1
            if x!=f[x]:
                f[x]=find(f[x])

            return f[x]

        def uni(x, y):
            nonlocal islands
            x,y=find(x),find(y)
            if x!=y: 
                f[x]=y
                islands-=1

        for i in range(len(stones)): uni(stones[i][0], ~stones[i][1])


        return len(stones)-islands