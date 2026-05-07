class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(s):
            return s == s[::-1]

        def get_all_partition(m, index, ans):
            if index == len(m):
                res.append([''.join(j for j in i) for i in ans])
                return

            for end in range(index, len(m)):
                if is_palindrome(m[index:end+1]):
                    ans.append(list(m[index:end+1]))
                    get_all_partition(m, end+1, ans)
                    ans.pop()

        get_all_partition(s, 0, [])

        return res
