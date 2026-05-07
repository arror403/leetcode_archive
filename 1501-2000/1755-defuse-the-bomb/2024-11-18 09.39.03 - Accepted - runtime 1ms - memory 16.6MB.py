class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        L=len(code)
        if k==0:
            return [0]*L
        elif k<0:
            k*=-1
            code.reverse()
            code+=code[:k]
            return [sum(code[i:i+k]) for i in range(1,L+1)][::-1]
        else:
            code+=code[:k]
            return [sum(code[i:i+k]) for i in range(1,L+1)]