class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def generateGrayarr(n):
            if n <= 0: return

            arr = ['0', '1']
            i = 2
            j = 0
            while 1:
                if i >= (1<<n): break
            
                for j in range(i-1, -1, -1):
                    arr.append(arr[j])

                for j in range(i):
                    arr[j] = "0" + arr[j]

                for j in range(i, 2 * i):
                    arr[j] = "1" + arr[j]

                i <<= 1

            return arr

        res = [int(x, 2) for x in generateGrayarr(n)]
        t=-1
        for i,v in enumerate(res):
            if v==start:
                t=i
                break
        
        
        return res[t:]+res[:t]