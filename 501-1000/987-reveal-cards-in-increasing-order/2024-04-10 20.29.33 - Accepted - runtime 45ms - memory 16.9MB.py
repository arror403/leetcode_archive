class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        L=len(deck)
        res=[0]*L
        x=list(range(L))
        pos = 0

        for i in deck:
            res[x.pop(0)]=i
            if x: x.append(x.pop(0))

        return res