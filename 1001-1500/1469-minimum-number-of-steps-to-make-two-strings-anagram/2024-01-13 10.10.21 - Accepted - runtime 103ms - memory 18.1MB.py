class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=Counter(s)
        return sum(v if k not in a.keys() else v-a[k] if v>a[k] else 0 for k,v in Counter(t).items())