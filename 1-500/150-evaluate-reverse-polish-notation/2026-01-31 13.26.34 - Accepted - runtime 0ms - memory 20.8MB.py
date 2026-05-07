class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            # operand (numbers)
            if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
                st.append(int(token))
            # operator
            else:
                val1 = st.pop()
                val2 = st.pop()

                if token == '+':
                    st.append(val2 + val1)
                elif token == '-':
                    st.append(val2 - val1)
                elif token == '*':
                    st.append(val2 * val1)
                elif token == '/':
                    tmp = val2/val1
                    if tmp < 0:
                        st.append(ceil(tmp))
                    else:
                        st.append(floor(tmp))

        return st.pop()