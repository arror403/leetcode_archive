class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=""
        x=0
        for i in range(len(word)):
            if word[i]==ch:
                x=i
                break

        for i in range(x+1): res+=word[i]
        # print(res)

        res=res[::-1]
    
        for i in range(x+1,len(word)): res+=word[i]

        return res