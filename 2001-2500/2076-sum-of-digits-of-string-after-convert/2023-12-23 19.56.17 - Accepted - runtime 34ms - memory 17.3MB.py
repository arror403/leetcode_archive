class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t=''.join([str(ord(i)-96) for i in s])
        for _ in range(k): t=sum(list(map(int,str(t))))
        return t