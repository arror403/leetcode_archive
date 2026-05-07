class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=0
        for op in logs:
            if op=="./": continue
            elif op=="../":
                if res>0: res-=1
                else: continue
            else: res+=1

        return res