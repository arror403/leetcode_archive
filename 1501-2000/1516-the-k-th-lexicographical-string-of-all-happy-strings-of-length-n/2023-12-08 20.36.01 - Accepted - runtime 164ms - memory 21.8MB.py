class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=self.generate_strings(n)
        return res[k-1] if len(res)>=k else ""



    ##### power by chatGPT #####
    def generate_strings(self, n):
        memo = {}

        def generate_helper(current_string):
            if len(current_string) == n:
                return [current_string]

            if current_string in memo:
                return memo[current_string]

            result = []
            for char in ['a', 'b', 'c']:
                if not current_string or current_string[-1] != char:
                    result.extend(generate_helper(current_string + char))

            memo[current_string] = result
            return result

        return generate_helper('')