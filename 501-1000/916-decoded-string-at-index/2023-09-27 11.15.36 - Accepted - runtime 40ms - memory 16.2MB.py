class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        current_length = 0

        for char in s:
            if char.isdigit():
                current_length *= int(char)
            else:
                current_length += 1

        for char in reversed(s):
            k %= current_length
            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                current_length /= int(char)
            else:
                current_length -= 1