class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        t=[0]+list(accumulate(differences))
        res=(upper-max(t))-(lower-min(t))+1

        return 0 if res<0 else res