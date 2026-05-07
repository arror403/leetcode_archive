class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        max_brainpower = max(questions, key=lambda x: x[1])[1]  # Maximum brainpower in the questions

        memo = [0] * (n + max_brainpower + 1)

        for i in range(n - 1, -1, -1):
            solve_score = questions[i][0]  # Points earned by solving the current question
            remaining_brainpower = questions[i][1]  # Remaining brainpower after solving the current question

            # Find the maximum score for the remaining questions after skipping the current question
            skip_score = memo[i + 1]

            # Find the maximum score for the remaining questions after solving the current question
            if i + remaining_brainpower + 1 < n + max_brainpower + 1:
                solve_remaining_score = memo[i + remaining_brainpower + 1]
                score = solve_score + solve_remaining_score
            else:
                score = solve_score

            # Store the maximum score in the memoization table
            memo[i] = max(score, skip_score)

        return memo[0]