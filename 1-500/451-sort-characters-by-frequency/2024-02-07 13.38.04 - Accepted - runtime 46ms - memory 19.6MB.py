class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        d=sorted(Counter(s).items(),key=lambda x:x[1],reverse=True)
        res=[list(repeat(c,f)) for c,f in d]
        # print(res)

        return ''.join(str(i) for j in res for i in j)