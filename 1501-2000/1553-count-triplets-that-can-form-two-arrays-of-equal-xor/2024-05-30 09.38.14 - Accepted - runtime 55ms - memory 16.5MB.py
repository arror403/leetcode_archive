class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        L=len(arr)
        res=0
        
        for i in range(L):
            xor=arr[i]
            
            for j in range(i+1, L):
                xor^=arr[j]
                
                if xor==0:
                    res+=j-i
                    
        return res