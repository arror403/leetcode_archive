class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        b=[]
        satisfaction.sort()
        for n in range(0,len(satisfaction)):
            index=1
            sum=0
            
            for i in satisfaction:
                sum+=index*i
                index+=1
            
            b.append(sum)
            
            satisfaction.remove(min(satisfaction))
            # print(satisfaction)
        if max(b)<0: return 0
        else : return max(b)
        