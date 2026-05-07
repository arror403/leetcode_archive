class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        res=[]
        for i in nums:
            if i%2==0:
                res.append(i)
        if len(res)==0: return -1

        for i in dict.fromkeys(res): d[i]=0
        for i in res: d[i]+=1
        # d=dict(sorted(d.items(), key=lambda x: x[1]))
        d=dict(sorted(d.items()))
        print(d)
        return max(d, key=d.get)