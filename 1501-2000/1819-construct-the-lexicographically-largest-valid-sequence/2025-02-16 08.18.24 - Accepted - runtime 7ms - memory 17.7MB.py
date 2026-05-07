class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans=[0]*(n*2-1)
        visited=[False]*(n+1)

        def calc(index, ans, visited, n):
            if index==len(ans):
                return True

            if ans[index]!=0:
                return calc(index+1, ans, visited, n)
                # value already assigned in this position. So go ahead with the next index.
            else:
                # we start from n to 1 since we need to find out the lexicographically largest sequence.
                for i in range(n,0,-1):
                # for (int i = n; i >= 1; i--):
                    if visited[i]: continue
                    visited[i]=True
                    ans[index]=i
                    if i==1:
                        if calc(index+1, ans, visited, n): return True

                    elif ((index+i)<len(ans) and ans[index+i]==0):
                        ans[i+index]=i
                # assigning the second occurence of i in the desired position i.e.(current index + i)
                        if calc(index+1, ans, visited, n):
                            return True 
                # largest possible sequence satisfying the given conditions found.
                        ans[index+i]=0

                    ans[index]=0
                    visited[i]=False

            return False


        calc(0, ans, visited, n)


        return ans