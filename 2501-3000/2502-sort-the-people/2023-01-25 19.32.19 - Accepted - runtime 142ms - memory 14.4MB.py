class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t=[]
        res=[]
        for i in range(len(names)):
            tmp=[names[i],heights[i]]
            t.append(tmp)
        # print (t)
        t=sorted(t, key = lambda t : t[1], reverse=True)
        for i in t:
            res.append(i[0])
        return res