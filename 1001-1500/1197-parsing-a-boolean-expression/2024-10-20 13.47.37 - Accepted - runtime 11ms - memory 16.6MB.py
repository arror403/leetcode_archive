class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s=[]
        for c in expression:
            if c==')':
                seen=set()
                while s[-1]!='(': seen.add(s.pop())
                s.pop()
                op=s.pop()
                s.append(all(seen) if op=='&' else any(seen) if op=='|' else not seen.pop())
            elif c!=',':
                s.append(True if c=='t' else False if c=='f' else c)


        return s.pop()