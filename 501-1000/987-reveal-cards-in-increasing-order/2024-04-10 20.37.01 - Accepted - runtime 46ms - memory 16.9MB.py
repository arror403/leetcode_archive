class Solution:
    ##### power by Claude #####
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        L=len(deck)
        deck.sort()
        x=deque(range(L))
        res=[0]*L

        for card in deck:
            res[x.popleft()]=card
            if x: x.append(x.popleft())

        return res