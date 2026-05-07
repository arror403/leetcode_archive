class Solution:
    def intersect(self, m: List[int], n: List[int]) -> List[int]:
        d1=Counter(m)
        d2=Counter(n)
        res=[]

        for k in d1.keys()&d2.keys():
            if d1[k]>d2[k]:
                res+=list(repeat(k,d2[k]))
            else:
                res+=list(repeat(k,d1[k]))

        return res