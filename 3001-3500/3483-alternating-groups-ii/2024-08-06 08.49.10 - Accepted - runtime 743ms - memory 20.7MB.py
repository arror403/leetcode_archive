class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        # Duplicate the array to handle circular nature
        colors+=colors
        # Count the number of non-alternating pairs in the first window
        non_alternating=sum(colors[i]==colors[i+1] for i in range(k-1))
        count=int(non_alternating==0)
        
        # Sliding window
        for i in range(1,n):
            # Remove the effect of the first pair
            if colors[i-1]==colors[i]:
                non_alternating-=1
            # Add the effect of the new pair
            if colors[i+k-2]==colors[i+k-1]:
                non_alternating+=1
            
            count+=1 if non_alternating==0 else 0
        
        
        return count