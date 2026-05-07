class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # unordered_map<int, int> mpr, mpc, mprc, mpcc
        mpr=defaultdict(int)
        mpc=defaultdict(int)
        mprc=defaultdict(int)
        mpcc=defaultdict(int)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mpr[mat[i][j]]=i
                mpc[mat[i][j]]=j

        for i in range(len(arr)):
            n=arr[i]
            mprc[mpr[n]]+=1
            mpcc[mpc[n]]+=1

            if (mprc[mpr[n]]==len(mat[0]) or mpcc[mpc[n]]==len(mat)):
                return i


        return -1