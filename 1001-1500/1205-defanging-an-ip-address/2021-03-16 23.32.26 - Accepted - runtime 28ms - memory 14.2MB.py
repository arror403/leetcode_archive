class Solution:
    def defangIPaddr(self, address: str) -> str:
        b=[]
        for i in range(0,len(address)):
            if address[i]!='.':
                b+=address[i]
            elif address[i]=='.':
                b+="[.]"
        b=''.join(b)
        return b