class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        
        for c in s:
            if c.islower():
                res.append(c)
            elif c=='*':
                if res:
                    res.pop()
                else:
                    continue
            elif c=='#':
                res+=res
            elif c=='%':
                res.reverse()
            else:
                # print("????")
                break
        

        return ''.join(res) if res else ""