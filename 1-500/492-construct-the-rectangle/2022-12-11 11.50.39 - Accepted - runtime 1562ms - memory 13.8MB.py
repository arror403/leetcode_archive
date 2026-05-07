class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # if area==2: return [2,1]
        # elif area==3: return [3,1]
        t=math.sqrt(area)
        if t*t==int(math.sqrt(area))**2:
            for i in range(int(t),area+1):
                print(i)
                if area%i==0:
                    return [i,int(area/i)]
        else:
            for i in range(int(t)+1,area+1):
                if area%i==0:
                    return [i,int(area/i)]