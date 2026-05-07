class Solution:
    def isValid(self, input: str) -> bool:
        s=[]
        for i in input:
            if i=="(":
                s.append("(")
            elif i=="[":
                s.append("[")
            elif i=="{":
                s.append("{")
                
            elif i==")":
                if s==[]:
                    return 0
                    break
                elif s[-1]=="(":
                    s.pop()
                else:
                    return 0
                    break
            elif i=="]":
                if s==[]:
                    return 0
                    break
                elif s[-1]=="[":
                    s.pop()
                else:
                    return 0
                    break
            elif i=="}":
                if s==[]:
                    return 0
                    break
                elif s[-1]=="{":
                    s.pop()
                else:
                    return 0
                    break

        if s==[]:
            return 1
        else:
            return 0
