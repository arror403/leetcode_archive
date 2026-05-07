class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        b=[]
        d = float('inf')
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<d:
                d=abs(arr[i]-arr[i+1])
            
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==d:
                tmp=[arr[i],arr[i+1]]
                b.append(tmp)
                
        return b