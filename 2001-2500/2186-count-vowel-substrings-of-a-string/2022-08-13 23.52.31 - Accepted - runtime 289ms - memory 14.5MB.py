class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        m=[word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1)]
        res=0
        # res=sorted(res,key=len)
        # print(res)
        
        for i in m:
            if len(i)<5: continue
            i=set(i)
            if 'a' in i and 'e' in i and 'i' in i and 'o' in i and 'u' in i and len(i)==5:
                res+=1
        
        return res
                