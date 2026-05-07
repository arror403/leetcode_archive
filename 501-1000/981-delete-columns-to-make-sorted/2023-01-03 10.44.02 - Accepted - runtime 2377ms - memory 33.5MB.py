import numpy as np

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        tmp=[]
        res=0
        for i in strs: tmp.append(list(i))
        tmp=np.array(tmp)
        # print(tmp)
        for i in range(len(tmp[0])):
            # print(list(tmp[:,i]))
            if list(tmp[:,i])!=sorted(list(tmp[:,i])):
                res+=1

        return res