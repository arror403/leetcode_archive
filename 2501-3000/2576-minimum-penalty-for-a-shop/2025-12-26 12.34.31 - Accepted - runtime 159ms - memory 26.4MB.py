class Solution:
    def bestClosingTime(self, customers: str) -> int:
        tx=list(accumulate([0]+[1 if c=='N' else 0 for c in customers]))
        ty=list(accumulate([0]+[1 if c=='Y' else 0 for c in customers[::-1]]))
        # print(tx, ty[::-1])
        # print(list(zip(tx,ty[::-1])))

        return min(enumerate(a+b for a,b in zip(tx,ty[::-1])), key=lambda x:x[1])[0]