class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        stack=[(0, target, [])]

        while stack:
            start, current_target, path = stack.pop()

            if current_target==0:
                res.append(path)
                continue

            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>current_target:
                    break

                new_target = current_target-candidates[i]
                new_path = path+[candidates[i]]
                stack.append((i+1, new_target, new_path))


        return res