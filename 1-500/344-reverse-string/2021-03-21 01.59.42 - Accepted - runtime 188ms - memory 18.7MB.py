class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp=''
        j=len(s)-1
        for i in range(0,int(len(s)/2)):
            tmp=s[i]
            s[i]=s[j]
            s[j]=tmp
            j-=1
        # print (s)