class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        def matrix_multiply(A, B, mod):
            """Multiply two matrices A and B with modulo."""
            n = len(A)
            C = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
                        
            return C

        def matrix_pow(A, power, mod):
            """Calculate A^power efficiently using binary exponentiation."""
            n = len(A)
            result = [[0] * n for _ in range(n)]
            
            # Initialize result to identity matrix
            for i in range(n):
                result[i][i] = 1
                
            # Binary exponentiation
            while power > 0:
                if power % 2 == 1:
                    result = matrix_multiply(result, A, mod)
                A = matrix_multiply(A, A, mod)
                power //= 2
                
            return result

        MOD = 10**9 + 7
        
        # Initialize character counts
        d = Counter(s)
        
        # Calculate the transformation matrix
        # Each character transforms to specific characters after t transforms
        if t > 0:
            # Create a transformation matrix (26x26)
            # matrix[i][j] means: after 1 transformation, 
            # how many characters j are produced from 1 character i
            matrix = [[0] * 26 for _ in range(26)]
            
            # Fill the transformation matrix
            for i in range(26):
                if i == 25:  # 'z'
                    matrix[i][0] = 1  # 'z' -> 'a'
                    matrix[i][1] = 1  # 'z' -> 'b'
                else:
                    matrix[i][i+1] = 1  # 'a'-'y' -> next letter
            
            # Fast matrix exponentiation to get transformation after t steps
            result_matrix = matrix_pow(matrix, t, MOD)
            
            # Apply the transformation
            new_d = Counter()
            for ch, count in d.items():
                if not ch.isalpha():
                    continue
                    
                ch_idx = ord(ch) - ord('a')
                for i in range(26):
                    if result_matrix[ch_idx][i] > 0:
                        new_d[chr(i + ord('a'))] += (count * result_matrix[ch_idx][i]) % MOD
                        new_d[chr(i + ord('a'))] %= MOD
            
            d = new_d
        
        return sum(d.values()) % MOD



        # d=Counter(s)

        # for _ in range(t):
        #     tmp=Counter()
        #     for i in range(25):
        #         if d[chr(97+i)]:
        #             tmp[chr(98+i)]=d[chr(97+i)]
        #     if d['z']:    
        #         tmp['a']=d['z']
        #         tmp['b']+=d['z']
        #     d=tmp


        # return d.total()%(10**9+7)