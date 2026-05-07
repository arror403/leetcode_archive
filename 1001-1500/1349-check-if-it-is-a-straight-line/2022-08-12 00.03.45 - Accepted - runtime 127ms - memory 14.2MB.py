class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0]==coordinates[1][0]:
            
            for i in coordinates:
                if i[0]==coordinates[0][0]: continue
                else: return False
                
            return True
        else:
            m=(coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
            b=coordinates[0][1]-m*(coordinates[0][0])

            # print(m,b)

            # y=m*x+b

            for i in coordinates:
                if i[0]*m+b==i[1]: continue
                else: return False

            return True