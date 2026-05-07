class Solution:
    def stringMatching(self, w: List[str]) -> List[str]:
        return list(dict.fromkeys(i for i,j in combinations(sorted(w,key=lambda x:len(x)),2) if i in j))