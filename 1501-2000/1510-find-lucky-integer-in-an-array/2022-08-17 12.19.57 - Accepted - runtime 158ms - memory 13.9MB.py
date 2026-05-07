class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res=[]
        for i in arr:
            if i==arr.count(i):
                res.append(i)
        
        return max(res) if len(res)!=0 else -1