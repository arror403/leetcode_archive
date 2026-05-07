class Solution:
    def makeFancyString(self, s: str) -> str:
        res=[]
        for k, g in itertools.groupby(s): #k for key, g for group
            # print (k,list(g),len(list(g)))
            l=len(list(g))
            print(l)
            if l<=2:
                for i in range(l):
                    res+=k
            else:
                for i in range(2):
                    res+=k

        return ''.join(res)