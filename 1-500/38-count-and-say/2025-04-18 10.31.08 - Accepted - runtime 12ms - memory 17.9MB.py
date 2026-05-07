class Solution:
    def countAndSay(self, n: int) -> str:
        # m=[1,11,21,1211,111221,312211,13112221,1113213211,31131211131221,13211311123113112211]

        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))


        return s