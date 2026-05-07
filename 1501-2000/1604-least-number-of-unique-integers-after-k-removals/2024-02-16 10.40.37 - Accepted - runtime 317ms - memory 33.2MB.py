class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        ##### improved by chatGPT #####

        counter = Counter(arr)
        frequencies = sorted(counter.values())

        res = len(counter)
        for f in frequencies:
            if f <= k:
                k -= f
                res -= 1
            else:
                break
        return res