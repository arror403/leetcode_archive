class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        L=len(target)
        s=set(target)
        i=0
        
        for x in range(1, n+1):
            if x in s:
                res.append("Push")
                i+=1
            else:
                res.append("Push")
                res.append("Pop")

            if i==L: break


        return res