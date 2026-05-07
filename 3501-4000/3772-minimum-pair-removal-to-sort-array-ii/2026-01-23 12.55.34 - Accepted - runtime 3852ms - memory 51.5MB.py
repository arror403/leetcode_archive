from sortedcontainers import SortedDict

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums[:]
        s = SortedList()
        nxt = []
        pre = []
        for i in range(n):
            nxt.append(i+1)
            pre.append(i-1)
        # insert all pairs into set
        cnt = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]: 
                cnt += 1
            s.add((a[i] + a[i+1], i))
        
        ans = 0
        while cnt:
            # int i = s.begin()->second;
            i = s.pop(0)[1]
            j = nxt[i]
            p = pre[i]
            q = nxt[j]
            # pair {i, j}
            if a[i] > a[j]: 
                cnt -= 1
            if p >= 0:
                # pair {p, i}
                if (a[p] > a[i] and a[p] <= a[i] + a[j]):
                    cnt -= 1
                elif (a[p] <= a[i] and a[p] > a[i] + a[j]):
                    cnt += 1
            if q < n:
                # pair {j, q}
                if (a[q] >= a[j] and a[q] < a[i] + a[j]):
                    cnt += 1
                elif (a[q] < a[j] and a[q] >= a[i] + a[j]):
                    cnt -= 1
            
            if p >= 0:
                # s.erase({a[p] + a[i], p})
                s.remove((a[p] + a[i], p))
                # s.insert({a[p] + a[i] + a[j], p})
                s.add((a[p] + a[i] + a[j], p))
            if q < n:
                # s.erase({a[j] + a[q], j})
                s.remove((a[j] + a[q], j))
                # s.insert({a[i] + a[j] + a[q], i})
                s.add((a[i] + a[j] + a[q], i))
                pre[q] = i

            nxt[i] = q
            a[i] = a[i] + a[j]
            ans += 1
        

        return ans