class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # d=sorted({i:v for i,v in enumerate(temperatures)}.items(), key=lambda x:x[1])
        ans = [0] * len(temperatures)
        stack = deque()
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans

