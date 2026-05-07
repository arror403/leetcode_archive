class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks=[c=="B" for c in blocks]
        s=[sum(blocks[i:i+k]) for i in range(len(blocks)-k+1)]

        return k-max(s)