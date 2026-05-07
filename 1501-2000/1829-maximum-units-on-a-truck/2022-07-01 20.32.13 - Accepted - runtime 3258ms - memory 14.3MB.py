class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sum=0
        # for i in boxTypes:
        #     i.append(i[1]/i[0])
            
        boxTypes=sorted(boxTypes,key=lambda l:l[1], reverse=True)
        
        for i in boxTypes:
            while (i[0]!=0) and (truckSize!=0):
                sum+=i[1]
                i[0]-=1
                truckSize-=1
                
        return sum