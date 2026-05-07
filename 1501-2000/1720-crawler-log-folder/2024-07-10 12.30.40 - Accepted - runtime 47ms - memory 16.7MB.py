class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        logs=[x for x in logs if x!="./"]
        for op in logs:
            if op!="../": res+=1
            elif res>0: res-=1

        return res