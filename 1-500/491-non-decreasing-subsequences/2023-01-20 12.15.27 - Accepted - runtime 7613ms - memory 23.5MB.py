class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def subsequences(ind,ans,l,n):
            final_ans = []
            if ind == n:
                return [ans]
            else:
                final_ans.extend(subsequences(ind+1,ans + [l[ind]],l,n))
                final_ans.extend(subsequences(ind+1,ans,l,n))
                return final_ans

        def non_decreasing(lst):
            for a, b in zip(lst, lst[1:]):
                if b < a:
                    return False
            return True
            
        res=[]
        t=subsequences(0,[],nums,len(nums))
        for i in t:
            if non_decreasing(i) and (len(i)>=2) and (i not in res):
                res.append(i)

        return res