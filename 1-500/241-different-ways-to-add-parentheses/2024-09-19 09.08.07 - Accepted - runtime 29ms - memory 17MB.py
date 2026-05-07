class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {'+': add, '-': sub, '*': mul}
        
        @lru_cache(maxsize=None)
        def compute(exp):
            if exp.isdigit():
                return [int(exp)]
            
            res=[]
            for i,c in enumerate(exp):
                if c in operators:
                    left = compute(exp[:i])
                    right = compute(exp[i+1:])
                    res.extend(operators[c](x,y) for x in left for y in right)
            
            return res


        return compute(expression)