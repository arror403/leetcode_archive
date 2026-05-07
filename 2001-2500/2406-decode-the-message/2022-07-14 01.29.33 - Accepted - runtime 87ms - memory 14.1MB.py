class Solution:
    def decodeMessage(self,key : str, message: str) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        b=""
        key=list(key)
        m=[]
        for i in key:
            if i not in m and i!=" ": 
                m.append(i)
        m=''.join(m)
        for i in message:
            if i.isalpha():
                b+=alpha[m.index(i)]
            elif i==" ":
                b+=" "
        return b     