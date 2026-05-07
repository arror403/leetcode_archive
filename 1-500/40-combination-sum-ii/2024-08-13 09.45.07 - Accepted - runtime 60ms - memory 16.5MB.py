class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tempList, cand, remain, start):
            nonlocal res
            if remain<0: 
                return  # no solution
            elif remain==0:
                res.append(tempList[:])
            else:
                for i in range(start, len(cand)):
                    if i>start and cand[i]==cand[i-1]: continue    # skip duplicates
                    
                    tempList.append(cand[i])
                    backtrack(tempList, cand, remain-cand[i], i+1)
                    tempList.pop()


        res=[]
        backtrack([], sorted(candidates), target, 0)

        return res