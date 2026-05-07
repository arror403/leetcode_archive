class Solution:
    def countMonobit(self, n: int) -> int:
        return bisect_right([0,1,3,7,15,31,63,127,255,511],n)