class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0]
        for i in range(1, len(target)):
            res += max(target[i] - target[i-1], 0)

        return res
        
        # res = min(target)

        # while set(target)!={0}:
        #     m = min(set(target)-{0})
        #     target = [v-m if v>0 else 0 for v in target]
        #     t = [max(list(g)) for k,g in groupby(target, key=lambda x: x!=0) if k!=0]
        #     res += m
        #     print(target, m)


        # return res