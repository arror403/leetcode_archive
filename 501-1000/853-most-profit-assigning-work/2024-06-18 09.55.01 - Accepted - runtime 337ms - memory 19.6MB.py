class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m=sorted(zip(difficulty,profit))
        worker.sort()
        res=0
        max_profit_so_far=0
        j=0

        for w in worker:
            while j<len(m) and w>=m[j][0]:
                max_profit_so_far=max(max_profit_so_far, m[j][1])
                j+=1
            res+=max_profit_so_far


        return res