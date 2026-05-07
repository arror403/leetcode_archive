class Solution:
    def maxLength(self, arr: List[str]) -> int:
        r=[]
        for i in range(1,len(arr)+1): r+=(itertools.combinations(arr,i))
        for i in range(len(r)): r[i]=''.join(r[i])
        r=sorted(r, key=len, reverse=True)
        for i in r:
            if len(list(i))==len(dict.fromkeys(list(i))):
                return len(i)
        return 0