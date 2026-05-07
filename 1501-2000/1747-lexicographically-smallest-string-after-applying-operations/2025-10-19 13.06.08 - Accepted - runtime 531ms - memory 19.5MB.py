class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue = deque([s])
        seen = {s}
        res = s

        while queue:
            current_s = queue.popleft()

            s_list = list(current_s)
            for i in range(1, len(s_list), 2):
                s_list[i] = str((int(s_list[i]) + a) % 10)
            
            s_add = ''.join(s_list)
            
            if s_add not in seen:
                seen.add(s_add)
                queue.append(s_add)
                res = min(res, s_add)

            s_rotate = current_s[b:] + current_s[:b]
            
            if s_rotate not in seen:
                seen.add(s_rotate)
                queue.append(s_rotate)
                res = min(res, s_rotate)


        return res