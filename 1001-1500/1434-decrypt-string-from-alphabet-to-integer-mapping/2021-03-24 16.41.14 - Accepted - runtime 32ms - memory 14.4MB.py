class Solution:
    def freqAlphabets(self, s: str) -> str:
        b=[]
        i=0
        while 1: 
            if i>=(len(s)): break
            if (s[i]=='1') & (i<=len(s)-3):
                if s[i+2]=='#':
                    if s[i+1]=='0':b.append('j')
                    elif s[i+1]=='1':b.append('k')
                    elif s[i+1]=='2':b.append('l')
                    elif s[i+1]=='3':b.append('m')
                    elif s[i+1]=='4':b.append('n')
                    elif s[i+1]=='5':b.append('o')
                    elif s[i+1]=='6':b.append('p')
                    elif s[i+1]=='7':b.append('q')
                    elif s[i+1]=='8':b.append('r')
                    elif s[i+1]=='9':b.append('s')
                    i+=3
                    if i<len(s): continue
            elif (s[i]=='2') & (i<=len(s)-3):
                if s[i+2]=='#':
                    if s[i+1]=='0':b.append('t')
                    elif s[i+1]=='1':b.append('u')
                    elif s[i+1]=='2':b.append('v')
                    elif s[i+1]=='3':b.append('w')
                    elif s[i+1]=='4':b.append('x')
                    elif s[i+1]=='5':b.append('y')
                    elif s[i+1]=='6':b.append('z')
                    i+=3
                    if i<len(s): continue
            if i<len(s):
                if s[i]=='1':b.append('a')
                elif s[i]=='2':b.append('b')
                elif s[i]=='3':b.append('c')
                elif s[i]=='4':b.append('d')
                elif s[i]=='5':b.append('e')
                elif s[i]=='6':b.append('f')
                elif s[i]=='7':b.append('g')
                elif s[i]=='8':b.append('h')
                elif s[i]=='9':b.append('i')
                i+=1
            
            
            
        ans=''.join(b)
        return ans
                