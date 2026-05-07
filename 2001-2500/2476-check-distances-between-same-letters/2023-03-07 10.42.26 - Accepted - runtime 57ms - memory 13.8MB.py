class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        r=[]
        res=True
        for i in range(len(s)):
            tmp=[s[i],i]
            r.append(tmp)
        r=sorted(r, key=lambda x:x[0])
        # print (r)
        for i in range(0,len(s),2):
            if (r[i+1][1]-r[i][1])-1==distance[ord(r[i][0])-97]:
                continue
            else:
                res=False
                break
        return res