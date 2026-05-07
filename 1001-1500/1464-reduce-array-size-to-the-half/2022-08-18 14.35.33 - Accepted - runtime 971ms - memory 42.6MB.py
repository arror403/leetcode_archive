class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d,res={},0
        for i in list(dict.fromkeys(arr)): d[i]=0
        for i in arr: d[i]+=1
        d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        # print(d)
        tmp=0
        for i in d:
            res+=1
            tmp+=d[i]
            if tmp>=(len(arr)//2):
                return res