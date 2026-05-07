class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        L=len(s)
        line=[0]*(L+1)
        s=list(s)

        for i in shifts:
            # forward shift so do +1
            if(i[2]==1):
                line[i[0]]+=1
                line[i[1]+1]-=1
            # backward shift so do -1
            else:
                line[i[0]]-=1
                line[i[1]+1]+=1

        for i in range(1,L+1):
            line[i]+=line[i-1]

        for i in range(L):
        # line[i] is how many times i have to change s[i], then adding it and taking modulo
            increaseBy=(ord(s[i])-97+line[i])%26
        # make abs()
            increaseBy=(increaseBy+26)%26
            s[i]=chr(increaseBy+97)


        return ''.join(s)