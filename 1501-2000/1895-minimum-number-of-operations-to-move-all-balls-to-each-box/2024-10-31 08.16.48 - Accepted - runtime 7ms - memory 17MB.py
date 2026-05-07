class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        L=len(boxes)
        res=[0]*L
        ops=0
        cnt=0

        for i in range(L):
            res[i]+=ops
            cnt+=1 if boxes[i]=='1' else 0
            ops+=cnt

        ops=0
        cnt=0

        for i in range(L-1,-1,-1):
            res[i]+=ops
            cnt+=1 if boxes[i]=='1' else 0
            ops+=cnt


        return res