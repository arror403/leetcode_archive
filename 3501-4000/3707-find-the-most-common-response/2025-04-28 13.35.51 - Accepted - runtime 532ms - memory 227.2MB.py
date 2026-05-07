class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        d=Counter(chain.from_iterable(set(r) for r in responses)).most_common()
        # print(d)

        # return ""
        return sorted(v for v,f in d if f==d[0][1])[0]