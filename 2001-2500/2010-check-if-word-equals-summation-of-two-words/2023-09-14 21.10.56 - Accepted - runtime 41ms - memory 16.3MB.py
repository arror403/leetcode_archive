class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
               
        def convert(t):
            return int(''.join([str(ord(i)-97) for i in list(t)]))

        return (convert(firstWord)+convert(secondWord))==convert(targetWord)