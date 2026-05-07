class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        
        def decode():
            nonlocal i
            res=""
            while i<len(s) and s[i]!=']':
                if not s[i].isdigit():
                    res+=s[i]
                    i+=1
                else:
                    n=0
                    while i<len(s) and s[i].isdigit():
                        n=n*10+int(s[i])
                        i+=1
                    
                    i+=1  # Skip '['
                    t=decode()  # Recursive call
                    i+=1  # Skip ']'
                    
                    res+=t*n  # Multiple string n times
            
            return res


        return decode()