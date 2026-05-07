class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        # function to get the result of the operation
        def perform(x, y, op):
            if op=='+': return x+y
            if op=='-': return x-y
            if op=='*': return x*y
            return 0

        res=[]
        isNumber=True
    
        for i in range(len(exp)):
            # check if current character is an operator
            if not exp[i].isnumeric():
                # if current character is not a digit then exp is not purely a number
                isNumber=False
                # list of first operands
                left = self.diffWaysToCompute(exp[:i])
                # list of second operands
                right = self.diffWaysToCompute(exp[i+1:])
                # performing operations
                for x in left:
                    for y in right:
                        res.append(perform(x, y, exp[i]))

        if isNumber: res.append(int(exp))


        return res