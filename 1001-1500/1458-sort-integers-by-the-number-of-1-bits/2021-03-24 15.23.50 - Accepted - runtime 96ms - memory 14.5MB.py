class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        b=[]
        ans=[]
        arr.sort()
        for i in arr:
            tmp=0
            while i!=0:
                if i%2==0:
                    i=int(i/2)
                else:
                    tmp+=1
                    i=int(i/2)
            b.append(tmp)
        # arr.sort()
            
        # print (b)
        for i in range(0,14):
            for j in range(0,len(arr)):
                if(b[j]==i):
                    ans.append(arr[j])
                    
        return ans
            