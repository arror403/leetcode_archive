class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                tmp=[arr[i],arr[j],arr[i]/arr[j]]
                res.append(tmp)

        res.sort(key=lambda row: row[2], reverse=False)
        
        return [res[k-1][0],res[k-1][1]]
                
                