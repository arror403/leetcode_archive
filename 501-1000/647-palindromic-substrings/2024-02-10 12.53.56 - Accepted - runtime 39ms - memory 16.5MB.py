class Solution:
    def countSubstrings(self, s: str) -> int:
        # from others solution
        ans,n,i=0,len(s),0

        while (i<n):
            j,k=i-1,i

            while k<n-1 and s[k]==s[k+1]: k+=1

            ans+=(k-j)*(k-j+1)//2

            i,k=k+1,k+1

            while ~j and k<n and s[k]==s[j]:
                j,k,ans=j-1,k+1,ans+1

        return ans