class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num=[str(i) for i in num]
        num=''.join(num)
        num=int(num)
        num+=k
        num=list(map(int,str(num)))
        return num