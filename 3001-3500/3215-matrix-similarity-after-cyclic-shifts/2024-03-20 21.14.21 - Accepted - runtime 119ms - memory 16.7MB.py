class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        def cyclic_shift(row, k, d):
            k%=len(row)
            return row[-k:]+row[:-k] if d=='right' else row[k:]+row[:k]
        
        t=[cyclic_shift(r,k,'left' if i%2==0 else 'right') for i,r in enumerate(mat)]
        
        return all(t[i][j]==mat[i][j] for i in range(len(mat)) for j in range(len(mat[0])))
