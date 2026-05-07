class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        w=[]
        res=[]
        for i in words:
            tmp=[0]*26
            for j in i:
                tmp[ord(j)-97]+=1
            w.append(tmp)
        
        for j in range(26):# r
            x=[]
            for i in range(len(w)):# c
                x.append(w[i][j])
            l=min(x)
            for k in range(l):
                res.append(chr(j+97))
                
        return res
            
        

        # res=[]
        # for i in range(97,124):
        #     f=1
        #     for w in words:
        #         if chr(i) in w:
        #             continue
        #         else:
        #             f=0
        #             break
        #     if f:
        #         res.append(chr(i))
        # return res