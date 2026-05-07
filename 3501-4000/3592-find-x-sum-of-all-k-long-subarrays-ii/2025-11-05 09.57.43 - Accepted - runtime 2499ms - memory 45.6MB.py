class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        cnt = defaultdict(int)
        
        # Use SortedList to simulate C++ set with custom comparator
        # Store as (-count, -value) for descending order
        top = SortedList()  # Top x elements
        bot = SortedList()  # Remaining elements
        running_sum = 0
        
        for i in range(len(nums)):
            # Handle the element being added to window
            count = cnt[nums[i]]
            
            if count > 0:
                # Remove old occurrence from either bot or top
                if (-count, -nums[i]) in bot:
                    bot.remove((-count, -nums[i]))
                else:
                    top.remove((-count, -nums[i]))
                    running_sum -= count * nums[i]
            
            # Update count and add to top
            cnt[nums[i]] = count + 1
            top.add((-(count + 1), -nums[i]))
            running_sum += (count + 1) * nums[i]
            
            # If top has more than x elements, move smallest to bot
            if len(top) > x:
                # Get the smallest element from top (last element due to sorting)
                neg_count, neg_val = top[-1]
                actual_count = -neg_count
                actual_val = -neg_val
                running_sum -= actual_count * actual_val
                bot.add((neg_count, neg_val))
                top.pop(-1)
            
            # Handle element leaving the window
            if i >= k:
                leaving_val = nums[i - k]
                count = cnt[leaving_val]
                
                # Remove from either bot or top
                if (-count, -leaving_val) in bot:
                    bot.remove((-count, -leaving_val))
                else:
                    top.remove((-count, -leaving_val))
                    running_sum -= count * leaving_val
                
                # Decrease count
                if count > 1:
                    bot.add((-(count - 1), -leaving_val))
                cnt[leaving_val] -= 1
                
                # If top has less than x elements, move largest from bot to top
                if len(top) < x and len(bot) > 0:
                    neg_count, neg_val = bot[0]
                    actual_count = -neg_count
                    actual_val = -neg_val
                    running_sum += actual_count * actual_val
                    top.add((neg_count, neg_val))
                    bot.pop(0)
            
            # Add result for complete windows
            if i + 1 >= k:
                res.append(running_sum)
        
        
        return res