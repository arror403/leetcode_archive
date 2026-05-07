class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res=cur=set()
        for i in arr:
            cur={i|j for j in cur}|{i}
            res|=cur


        return len(res)