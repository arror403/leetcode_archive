class Solution:
    def partitionString(self, s: str) -> int:
        ##### improved by chatGPT #####
        m = [0] * 26
        res = 1

        for i in s:
            if m[ord(i) - 97] == 0:
                m[ord(i) - 97] = 1
            else:
                m = [0] * 26
                res += 1
                m[ord(i) - 97] = 1

        return res