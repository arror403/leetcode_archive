class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Solves the problem using Breadth-First Search (BFS) to explore all reachable strings.

        1. Start with the initial string `s`.
        2. Use a queue to keep track of strings to visit.
        3. Use a 'seen' set to avoid processing the same string multiple times.
        4. In each step, take a string from the queue, apply the two operations (add and rotate)
           to generate two new candidate strings.
        5. If a new string hasn't been seen before, add it to the queue and the 'seen' set,
           and update our overall best result.
        """
        
        # The queue will hold all the strings we need to visit.
        queue = collections.deque([s])
        # The 'seen' set will store strings we have already added to the queue,
        # preventing cycles and redundant work.
        seen = {s}
        # 'res' will keep track of the lexicographically smallest string found so far.
        res = s

        while queue:
            # Get the next string to process.
            current_s = queue.popleft()

            # --- Apply Operation 1: Add 'a' to odd indices ---
            # It's easier to work with a list of characters for modification.
            s_list = list(current_s)
            for i in range(1, len(s_list), 2):
                # Convert char to int, add 'a', take modulo 10, and convert back to char.
                s_list[i] = str((int(s_list[i]) + a) % 10)
            
            s_add = "".join(s_list)
            
            # If we have found a new unique string
            if s_add not in seen:
                seen.add(s_add)
                queue.append(s_add)
                # Update the result if this new string is smaller.
                res = min(res, s_add)

            # --- Apply Operation 2: Rotate the string by 'b' ---
            # This is the correct way to perform a left rotation.
            s_rotate = current_s[b:] + current_s[:b]
            
            # If we have found a new unique string
            if s_rotate not in seen:
                seen.add(s_rotate)
                queue.append(s_rotate)
                # Update the result if this new string is smaller.
                res = min(res, s_rotate)


        return res


        
    # def findLexSmallestString(self, s: str, a: int, b: int) -> str:

    #     res=s
    #     t=[int(x) for x in s]
    #     seen=set()

    #     for i in range(len(s)*100):
    #         tmp=[]
    #         for j,v in enumerate(t):
    #             if j%2:
    #                 tmp.append((v+a)%10)
    #             else:
    #                 tmp.append(v)
    #         print(tmp)
    #         tmp=''.join([str(x) for x in tmp])
    #         if tmp not in seen:
    #             seen.add(tmp)
    #             res=min(res, tmp)
    #         print(t)
    #         t=t[:b]+t[b:]


    #     return res