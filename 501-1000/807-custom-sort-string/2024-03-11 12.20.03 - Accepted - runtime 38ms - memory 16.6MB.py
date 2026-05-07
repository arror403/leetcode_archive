class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count=Counter(s)
        result=[]
        for c in order: result.append(c*count.pop(c,0))
        result+=[c*f for c,f in count.items()]
        return ''.join(result)