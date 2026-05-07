class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        res = []
        sorted_vowels = []
        sorted_vowels_index = 0

        for char in s:
            if char in vowels:
                sorted_vowels.append(char)
                res.append('#')
            else:
                res.append(char)

        sorted_vowels.sort()

        for i, char in enumerate(res):
            if char == '#':
                res[i] = sorted_vowels[sorted_vowels_index]
                sorted_vowels_index += 1

        return ''.join(res)