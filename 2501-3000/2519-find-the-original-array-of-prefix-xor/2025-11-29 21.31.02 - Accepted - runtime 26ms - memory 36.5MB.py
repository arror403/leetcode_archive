class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res=[pref[0]]

        i=0
        for v in pref[1:]:
            res.append(pref[i]^v)
            i+=1

        return res