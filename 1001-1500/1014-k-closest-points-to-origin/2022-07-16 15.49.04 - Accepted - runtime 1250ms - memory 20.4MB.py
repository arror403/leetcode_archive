class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        w=[]
        res=[]
        for i in points:
            tmp=[i,(i[0]**2+i[1]**2)]
            w.append(tmp)    
            
        w.sort(key=lambda row: (row[1]), reverse=False)
        
        for i in range(k): res.append(w[i][0])
            
        return res