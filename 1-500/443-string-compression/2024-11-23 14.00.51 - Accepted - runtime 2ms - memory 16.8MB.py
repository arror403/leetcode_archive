class Solution:
    def compress(self, chars: List[str]) -> int:
        indexAns = index = 0
        while index < len(chars):
            currentChar = chars[index]
            count = 0
            while index < len(chars) and chars[index] == currentChar:
                index += 1
                count += 1

            chars[indexAns] = currentChar
            indexAns += 1

            if count != 1 :
                for c in list(str(count)):
                    chars[indexAns] = c
                    indexAns += 1


        return indexAns