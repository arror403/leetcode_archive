class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        mp = defaultdict(list)

        for i in range(n):
            mp[nums[i]].append(i)

        for v,l in mp.items():
            if len(l)<3: continue

            # Compute distance for first triplet
            id1, id2, id3 = l[0], l[1], l[2]
            res = min(res, (id3-id1)*2)

            # Slide the window of size 3 across the list
            for i in range(3, len(l)):
                id1 = id2
                id2 = id3
                id3 = l[i]
                res = min(res, (id3-id1)*2)


        return -1 if res==inf else res