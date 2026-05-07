class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate_postfix(expression):
            stack = []
            operators = set(['+', '-', '*', '/'])

            for token in expression:
                if token not in operators:
                    stack.append(int(token))
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if token == '+':
                        stack.append(operand1 + operand2)
                    elif token == '-':
                        stack.append(operand1 - operand2)
                    elif token == '*':
                        stack.append(operand1 * operand2)
                    elif token == '/':
                        stack.append(int(operand1/operand2))

            return stack[0]
        
        return evaluate_postfix(tokens)