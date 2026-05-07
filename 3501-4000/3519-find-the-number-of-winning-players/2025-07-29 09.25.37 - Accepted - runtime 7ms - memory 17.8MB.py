class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        b=defaultdict(Counter)

        for i,p in enumerate(pick):
            b[p[0]][p[1]]+=1

        # print(b)
        return sum(1 for i in b.keys() if max(b[i].values())>i)