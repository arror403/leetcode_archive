class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, current_combination):
            if len(current_combination) == len(digits):
                combinations.append(''.join(current_combination))
                return

            for letter in mapping[digits[index]]:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()

        combinations = []
        backtrack(0, [])
        return combinations