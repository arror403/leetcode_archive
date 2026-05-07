class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # d = {l: 0 for l in string.ascii_lowercase}
        a=Counter(s)
        b=Counter(t)
        res=0

        for k,v in b.items():
            if k not in a.keys():
                res+=v
            elif a[k]<v:
                res+=v-a[k]

        return res