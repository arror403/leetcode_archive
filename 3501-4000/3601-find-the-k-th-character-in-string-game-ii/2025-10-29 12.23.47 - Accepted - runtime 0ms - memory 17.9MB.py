class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        i = ceil(log2(k))
        n = 2**i
        d = 0

        while n > 1:
            if k > n // 2:
                k -= n // 2
                d += operations[i - 1]
            n //= 2
            i -= 1


        return chr(d%26 + 97)


        ##### original MLE approach #####

        # t = ceil(log2(k))
        # x = 0
        # d = {chr(i):chr(i+1) for i in range(97, 123)}
        # d['z'] = 'a'
        # word = "a"

        # for op in operations:
        #     if x < t:
        #         x += 1
        #     else:
        #         break
        #     if op == 0:
        #         word += word
        #     else:
        #         word += ''.join([d[c] for c in word])

        # return word[k-1]