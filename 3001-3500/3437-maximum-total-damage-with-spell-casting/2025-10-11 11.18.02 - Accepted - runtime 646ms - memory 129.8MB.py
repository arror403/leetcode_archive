class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        frequencyMap = Counter(power)  # Keep as dictionary
        uniquePowers = sorted(frequencyMap.keys())
        dp = [-1]*len(uniquePowers)
        
        def getMaxDamage(index):
            if index == len(uniquePowers):
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            # Option 1: Skip the current element
            skip = getMaxDamage(index + 1)
            
            # Option 2: Take the current element
            nextIndex = index + 1
            while nextIndex<len(uniquePowers) and (uniquePowers[nextIndex]-uniquePowers[index])<=2:
                nextIndex += 1
            
            take = frequencyMap[uniquePowers[index]] * uniquePowers[index] + getMaxDamage(nextIndex)
            
            dp[index] = max(take, skip)
            return dp[index]
        

        return getMaxDamage(0)

        # def getMaxDamage(dp, frequencyMap, uniquePowers, index):
        #     if index==len(uniquePowers): return 0
        #     # Option 1: Skip the current element
        #     if dp[index]!=-1: return dp[index]
        #     # Option 2: Take the current element
        #     skip = getMaxDamage(dp, frequencyMap, uniquePowers, index + 1)
        #     take = 0
        #     nextIndex = index + 1
        #     while nextIndex<len(uniquePowers) and (uniquePowers[nextIndex]-uniquePowers[index])<=2:
        #         nextIndex+=1
        #     take = frequencyMap[uniquePowers[index]]*uniquePowers[index] + getMaxDamage(dp, frequencyMap, uniquePowers, nextIndex)
        #     dp[index] = max(take, skip)
        #     return dp[index]


        # return getMaxDamage(dp, frequencyMap, uniquePowers, 0)