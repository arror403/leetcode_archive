class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2==p3==p4: return 0
        l=[]
        l.append(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
        l.append(math.sqrt((p1[0]-p3[0])**2+(p1[1]-p3[1])**2))
        l.append(math.sqrt((p1[0]-p4[0])**2+(p1[1]-p4[1])**2))
        l.append(math.sqrt((p2[0]-p3[0])**2+(p2[1]-p3[1])**2))
        l.append(math.sqrt((p2[0]-p4[0])**2+(p2[1]-p4[1])**2))
        l.append(math.sqrt((p3[0]-p4[0])**2+(p3[1]-p4[1])**2))
        # print(l)
        l.sort()
        return (l[0]==l[1]==l[2]==l[3] and l[4]==l[5])
    