class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        z=len([i for i in arr if i==0])
        L=len(arr)

        while 1:
            if arr[i]==0:
                arr.insert(i, 0)
                i+=1
            
            i+=1
            if (L+z)==len(arr): break
        
        for i in range(z): arr.pop()