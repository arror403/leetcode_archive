class Solution:
    def calculate(self, s: str) -> int:
        
        def shunting_yard(infix):
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            output = []
            operator_stack = []
            operators = set(['+','-','*','/'])

            # Helper function to check if a token is an operator
            def is_operator(token):
                return token in operators

            i = 0
            while i < len(infix):
                if infix[i].isdigit():
                    num = ''
                    while i < len(infix) and infix[i].isdigit():
                        num += infix[i]
                        i += 1
                    output.append(num)
                elif infix[i] in operators:
                    while (operator_stack and is_operator(operator_stack[-1]) and
                        precedence[infix[i]] <= precedence[operator_stack[-1]]):
                        output.append(operator_stack.pop())
                    operator_stack.append(infix[i])
                    i += 1
                else:
                    i += 1

            while operator_stack:
                output.append(operator_stack.pop())

            return output

        def evaluate_postfix(expression):
            stack = []

            for token in expression:
                if token.isdigit():
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
                        stack.append(int(operand1 / operand2))

            return stack[0]

        return evaluate_postfix(shunting_yard(s))