class Solution:
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):

        def bellman(best, pairs, rates):
            for _ in range(len(pairs)):
                for i in range(len(pairs)):
                    best[pairs[i][1]] = max(best[pairs[i][1]], best[pairs[i][0]]*rates[i])
                    best[pairs[i][0]] = max(best[pairs[i][0]], best[pairs[i][1]]/rates[i])

        best=defaultdict(float)
        best[initialCurrency]=1
        bellman(best, pairs1, rates1)
        bellman(best, pairs2, rates2)


        return best[initialCurrency]