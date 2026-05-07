class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res=[0]*len(queries)
        queriesPair=[]
        itemIndex=maxBeauty=0

        for i in range(len(queries)): queriesPair.append([queries[i], i])
        
        queriesPair.sort()
        items.sort()
        
        for i in range(len(queriesPair)):
            maxPriceAllowed = queriesPair[i][0]
            queryOriginalIndex = queriesPair[i][1]
            
            # // Iterate over items, stop when the price exceeds query price or no item left
            while (itemIndex<len(items) and items[itemIndex][0]<=maxPriceAllowed):
                maxBeauty = max(maxBeauty, items[itemIndex][1])
                itemIndex+=1
            
            res[queryOriginalIndex] = maxBeauty
        

        return res