class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        t=[]
        for i in dict.fromkeys(arr): d[i]=0
        for i in arr: d[i]+=1
        print(d)
        for k,v in d.items():
            if v not in t:
                t.append(v)
            else:
                return False
        return True