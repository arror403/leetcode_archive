class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        b=[]
        c=[]
        x=0
        for i in mat:
            tmp=[x,sum(i)]
            b.append(tmp)
            x+=1
        # print(b)    
        b.sort(key=lambda row: (row[1]), reverse=False)
        
        for i in range(k):
            c.append(b[i][0])
        
        
        return c