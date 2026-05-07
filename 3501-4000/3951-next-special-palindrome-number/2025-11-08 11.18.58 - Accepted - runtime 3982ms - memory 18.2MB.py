class Solution:
    def specialPalindrome(self, n: int) -> int:
        l = [[1], [2]*2, [3]*3, [4]*4, [5]*5, [6]*6, [7]*7, [8]*8, [9]*9]
        res = set()

        for d in range(1, 5):
            for c in combinations(l, d):
                t = list(chain.from_iterable(c))

                if len(t) > 15:
                    continue
                
                if len(set(t) & {1, 3, 5, 7, 9}) > 1:
                    continue
                
                # --- START OF THE EFFICIENT METHOD ---

                # 1. Count the occurrences of each digit
                counts = Counter(t)
                
                # 2. Find the middle digit (if any) and create the list for the first half
                middle_char = tuple()
                first_half = []
                
                for digit, count in counts.items():
                    if count % 2 != 0:
                        middle_char = (digit,)
                    # Add half of the digits to our list to be permuted
                    first_half.extend([digit] * (count // 2))
                
                # 3. Generate unique permutations of the much smaller first_half
                # Using a set gets unique permutations automatically
                for p_half in set(permutations(first_half)):
                    
                    # 4. Construct the full palindrome and add to results
                    # p_half + middle_char + reversed p_half
                    palindrome_tuple = p_half + middle_char + p_half[::-1]
                    res.add(palindrome_tuple)
                    
        res_as_ints = sorted([int(''.join([str(i) for i in x])) for x in res])


        for v in res_as_ints:
            if v>n:
                return v

        return 2666888888886662