class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[defaultdict(int)]
        i,n=0,len(formula)

        while i<n:
            if formula[i]=='(':
                stack.append(defaultdict(int))
                i+=1
            elif formula[i]==')':
                i+=1
                start = i

                while i<n and formula[i].isdigit(): i+=1

                multiplier = int(formula[start:i] or 1)
                top = stack.pop()

                for atom,count in top.items(): stack[-1][atom]+=count*multiplier

            else:
                start=i
                i+=1

                while i<n and formula[i].islower(): i+=1

                atom=formula[start:i]
                start=i

                while i<n and formula[i].isdigit(): i+=1
                
                count = int(formula[start:i] or 1)
                stack[-1][atom]+=count

        # Get the final counts from the stack
        res=stack.pop()
        # Sort by atom name and format the result
        return ''.join(f"{a}{(res[a]>1 and res[a] or '')}" for a in sorted(res))