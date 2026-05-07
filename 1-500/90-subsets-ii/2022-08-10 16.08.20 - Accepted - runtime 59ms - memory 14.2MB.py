class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        tmp=[sorted(j) for i in range(len(nums)+1) for j in itertools.combinations(nums,i)]
        for i in tmp: 
            if i not in res: 
                res.append(i)
        
        # print(res)
        return res