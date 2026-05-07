class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>y:
            first, second='a', 'b'
            first_score, second_score = x, y
        else:
            first, second='b', 'a'
            first_score, second_score = y, x

        s,score1 = self.remove_pairs(s, first, second, first_score)
        dummy,score2 = self.remove_pairs(s, second, first, second_score)

        return score1+score2


    def remove_pairs(self, s, first, second, score):
        stack=[]
        total_score=0
        for c in s:
            if stack and (stack[-1],c)==(first,second):
                stack.pop()
                total_score+=score
            else:
                stack.append(c)
        
        return ''.join(stack), total_score