class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Maximize: replace the first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num  # all digits are 9

        # Minimize: replace the first digit with 1 if it's not 1
        # otherwise find a non-0/1 digit (not first) to replace with 0
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch not in {'0', '1'}:
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num  # all digits are 0 or 1

        return max_num - min_num