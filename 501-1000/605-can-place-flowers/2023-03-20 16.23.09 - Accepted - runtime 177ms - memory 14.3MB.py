class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # for i in range(1,len(flowerbed)):
        #     if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
        #         flowerbed[i]=1
        #         n-=1
        # return n==0





        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0