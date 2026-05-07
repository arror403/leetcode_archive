class Solution:
    def hardestWorker(self, n: int, l: List[List[int]]) -> int:
        E=[e[0] for e in l]
        U=[l[0][1]]+[l[i+1][1]-l[i][1] for i in range(len(l)-1)]

        return min([x[0] for x in zip(E,U) if x[1]==max(U)])