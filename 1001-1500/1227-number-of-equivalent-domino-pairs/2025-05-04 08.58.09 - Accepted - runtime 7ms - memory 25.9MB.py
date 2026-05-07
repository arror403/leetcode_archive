class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m=[]

        for a,b in dominoes:
            if a>b: a,b=b,a
            m.append((a,b))


        return sum(f*(f-1)//2 for f in Counter(m).values() if f>1)