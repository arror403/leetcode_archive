class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [v^pref[i-1] for i,v in enumerate(pref[1:], start=1)]