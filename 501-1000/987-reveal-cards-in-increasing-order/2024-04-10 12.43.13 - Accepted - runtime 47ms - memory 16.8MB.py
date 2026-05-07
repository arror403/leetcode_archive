class Solution:
    ##### improved by chatGPT #####
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        L = len(deck)
        res = [0] * L
        indexes = list(range(L))
        pos = 0

        for card in deck:
            res[indexes.pop(0)] = card
            if indexes:
                indexes.append(indexes.pop(0))

        return res
        # deck.sort()
        # L=len(deck)
        # x=list(range(L))
        # res=[0]*L
        # i=0
        # j=0
        # p=2

        # while x:
        #     if i<L:
        #         res[i]=deck[j]
        #         x.remove(i)
        #         i+=p
        #         j+=1
        #     else:
        #         i=x[0]
        #         p*=2

        # return res