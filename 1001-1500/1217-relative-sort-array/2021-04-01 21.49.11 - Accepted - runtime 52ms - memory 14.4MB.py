class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        b=[]
        tmp=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    b.append(j)

        for i in arr1:
            if not(i in b):
                tmp.append(i)
        
        tmp.sort()
        for i in tmp:
            b.append(i)
            
        return b
                    
        