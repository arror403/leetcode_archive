class Solution:
    def minimizeResult(self, expression: str) -> str:
        def evaluate_math_expression(expr):
            # Handle implicit multiplication in various cases
            expr = re.sub(r'(\d)\(', r'\1*(', expr)  # 2( -> 2*(
            expr = re.sub(r'\)(\d)', r')*\1', expr)  # )2 -> )*2
            expr = re.sub(r'\)\(', r')*(', expr)     # )( -> )*(
            return eval(expr)
        
        l,r=expression.split('+')
        lp,rp=[],[]
        m=inf
        res=''

        for i in range(len(l)): lp.append(l[:i]+'('+l[i:])

        for i in range(1,len(r)+1): rp.append(r[:i]+')'+r[i:])

        for a in lp:
            for b in rp:
                print(a+"+"+b)
                tmp=evaluate_math_expression(a+'+'+b)
                if tmp<m:
                    m=tmp
                    res=a+'+'+b


        return res