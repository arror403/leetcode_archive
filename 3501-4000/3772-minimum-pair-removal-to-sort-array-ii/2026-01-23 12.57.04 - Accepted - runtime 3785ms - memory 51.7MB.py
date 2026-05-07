from sortedcontainers import SortedList

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        # Copy nums to a array
        a = nums[:]
        
        # Use SortedList instead of SortedDict.
        # It stores tuples: (sum_of_pair, left_index_of_pair)
        # This mimics set<pair<ll, int>> in C++ exactly.
        s = SortedList()

        # Doubly linked list simulation
        nxt = [i + 1 for i in range(n)]
        pre = [i - 1 for i in range(n)]

        # Initialize
        cnt = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]: 
                cnt += 1
            # Add the tuple (sum, index)
            s.add((a[i] + a[i+1], i))
        
        ans = 0
        
        while cnt > 0:
            # Get the pair with the smallest sum
            # s[0] gives the tuple (sum, index)
            # pop(0) removes and returns it
            val, i = s.pop(0)
            
            j = nxt[i]
            p = pre[i]
            q = nxt[j]
            
            # Cache values before modifying array or set to ensure consistency
            val_i = a[i]
            val_j = a[j]
            new_sum = val_i + val_j
            
            # --- Update Inversion Count (cnt) ---
            
            # 1. Check the pair being merged
            if val_i > val_j: 
                cnt -= 1
            
            # 2. Check the left neighbor (p)
            if p >= 0:
                val_p = a[p]
                # Was it an inversion before? (p > i)
                was_inv = val_p > val_i
                # Is it an inversion now? (p > new_merged_node)
                is_inv = val_p > new_sum
                
                if was_inv and not is_inv:
                    cnt -= 1
                elif not was_inv and is_inv:
                    cnt += 1
                
                # Remove the old connection (p, i) from SortedList
                # We must match the exact tuple (sum, index)
                s.remove((val_p + val_i, p))
                
                # Add the new connection (p, i_merged)
                s.add((val_p + new_sum, p))
            
            # 3. Check the right neighbor (q)
            if q < n:
                val_q = a[q]
                # Was it an inversion before? (j > q)
                was_inv = val_j > val_q
                # Is it an inversion now? (new_merged_node > q)
                is_inv = new_sum > val_q
                
                if was_inv and not is_inv:
                    cnt -= 1
                elif not was_inv and is_inv:
                    cnt += 1

                # Remove the old connection (j, q) from SortedList
                s.remove((val_j + val_q, j))
                
                # Add the new connection (i_merged, q)
                s.add((new_sum + val_q, i))
                
                # Update linked list back-pointer
                pre[q] = i

            # --- Apply Merge Changes ---
            
            # Update linked list forward-pointer
            nxt[i] = q
            
            # Update value in array
            a[i] = new_sum
            
            ans += 1

        return ans