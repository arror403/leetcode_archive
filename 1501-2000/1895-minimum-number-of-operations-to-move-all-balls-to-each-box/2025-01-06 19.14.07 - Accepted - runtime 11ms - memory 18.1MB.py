class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        L=len(boxes)
        res=[0]*L

        ops=cnt=0
        for i in range(L):
            res[i]+=ops
            cnt+=int(boxes[i]=='1')
            ops+=cnt

        ops=cnt=0
        for i in range(L-1,-1,-1):
            res[i]+=ops
            cnt+=int(boxes[i]=='1')
            ops+=cnt


        return res