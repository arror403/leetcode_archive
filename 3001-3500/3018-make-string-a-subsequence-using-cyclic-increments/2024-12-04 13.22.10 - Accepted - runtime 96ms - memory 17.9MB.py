class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        s="abcdefghijklmnopqrstuvwxyz"
        d={c:i for i,c in enumerate(s)}

        while i<len(str1) and j<len(str2):
            if str1[i]==str2[j] or s[(d[str1[i]]+1)%26]==str2[j]:
                i+=1
                j+=1
            else:
                i+=1

        return j==len(str2)