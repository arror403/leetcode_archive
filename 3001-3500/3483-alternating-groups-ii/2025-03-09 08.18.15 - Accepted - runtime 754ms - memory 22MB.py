class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        L=len(colors)
        colors+=colors
        non_alternating=sum(colors[i]==colors[i+1] for i in range(k-1))
        res=int(non_alternating==0)
        
        for i in range(1,L):
            if colors[i-1]==colors[i]:
                non_alternating-=1
            if colors[i+k-2]==colors[i+k-1]:
                non_alternating+=1
            
            res+=int(non_alternating==0)
        
        
        return res