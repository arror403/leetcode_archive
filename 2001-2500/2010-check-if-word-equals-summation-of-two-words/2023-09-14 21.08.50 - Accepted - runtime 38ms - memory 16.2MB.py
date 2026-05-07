class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a=int(''.join([str(ord(i)-97) for i in list(firstWord)]))
        b=int(''.join([str(ord(i)-97) for i in list(secondWord)]))
        c=int(''.join([str(ord(i)-97) for i in list(targetWord)]))
        return (a+b)==c
               