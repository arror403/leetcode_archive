class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res, i, j = 0, 0, 0

        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                res += 1
                i += 1
            j += 1


        return res