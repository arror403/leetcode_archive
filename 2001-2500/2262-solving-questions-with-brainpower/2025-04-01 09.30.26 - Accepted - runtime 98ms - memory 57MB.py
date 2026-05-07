class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        max_brainpower = max(questions, key=lambda x: x[1])[1]
        res = [0] * (n + max_brainpower + 1)

        for i in range(n-1, -1, -1):
            solve_score = questions[i][0] 
            remaining_brainpower = questions[i][1]
            skip_score = res[i + 1]

            if i + remaining_brainpower + 1 < n + max_brainpower + 1:
                solve_remaining_score = res[i + remaining_brainpower + 1]
                score = solve_score + solve_remaining_score
            else:
                score = solve_score

            res[i] = max(score, skip_score)


        return res[0]