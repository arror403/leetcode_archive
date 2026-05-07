class Solution:
    ##### power by Claude #####
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []
        for char in order:
            result.append(char * count.pop(char, 0))
        result.extend(char * count[char] for char in sorted(count))
        return ''.join(result)