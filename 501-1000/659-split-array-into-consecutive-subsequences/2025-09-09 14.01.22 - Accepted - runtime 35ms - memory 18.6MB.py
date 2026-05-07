class Solution:
    def isPossible(self, nums: List[int]) -> bool:        
        left=defaultdict(int)
        end=defaultdict(int)
        
        for i in nums: left[i]+=1
        
        for i in nums:
            if left[i]==0: continue
            left[i]-=1

            if end[i-1]>0:
                end[i-1]-=1
                end[i]+=1
            elif left[i+1]>0 and left[i+2]>0:
                left[i+1]-=1
                left[i+2]-=1
                end[i+2]+=1
            else:
                return False


        return True