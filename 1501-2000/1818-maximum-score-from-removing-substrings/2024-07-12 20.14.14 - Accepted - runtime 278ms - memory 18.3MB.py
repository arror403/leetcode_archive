class Solution:
    ##### by chatGPT #####
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if y > x:
            x, y = y, x
            high_pair, low_pair = 'ba', 'ab'
        else:
            high_pair, low_pair = 'ab', 'ba'

        def calculate_score(s, pair_value, pair):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == pair[0] and c == pair[1]:
                    stack.pop()
                    score += pair_value
                else:
                    stack.append(c)
            return ''.join(stack), score

        s, high_score = calculate_score(s, x, high_pair)
        _, low_score = calculate_score(s, y, low_pair)

        return high_score + low_score