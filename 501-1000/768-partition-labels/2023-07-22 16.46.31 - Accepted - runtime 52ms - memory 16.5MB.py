class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: i for i, char in enumerate(s)}
        print (last)
        start, end = 0, 0
        result = []
        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result