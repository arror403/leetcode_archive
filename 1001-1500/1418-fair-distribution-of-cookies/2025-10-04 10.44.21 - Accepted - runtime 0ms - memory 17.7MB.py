class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # Our best answer found so far, initialized to infinity.
        self.res = inf
        
        # Optimization 2: Sort cookies in descending order.
        # This helps in pruning more effectively and finding a good
        # candidate answer faster.
        cookies.sort(reverse=True)

        # A list to store the sum of cookies for each of the k children.
        distribution = [0] * k

        self.solve(0, distribution, cookies, k)
        
        return self.res

    def solve(self, cookie_idx, distribution, cookies, k):
        # Base case: if all cookies have been distributed.
        if cookie_idx == len(cookies):
            # We have a complete distribution. The unfairness is max(distribution).
            # We update our global result with the minimum unfairness found.
            self.res = min(self.res, max(distribution))
            return

        # Optimization 1: Pruning
        # If the current maximum cookie sum for any child is already
        # >= our best answer so far, there's no way this path can lead
        # to a better solution. So, we stop exploring this path.
        if max(distribution) >= self.res:
            return

        # Recursive step: Try to give the current cookie (cookies[cookie_idx])
        # to each of the k children.
        for i in range(k):
            # Give the cookie to child i
            distribution[i] += cookies[cookie_idx]

            # Recurse to distribute the next cookie
            self.solve(cookie_idx + 1, distribution, cookies, k)

            # Backtrack: take the cookie back from child i to explore other options
            distribution[i] -= cookies[cookie_idx]
            
            # Optimization 3: Symmetry Breaking
            # If this child had 0 cookies before we added the current one,
            # then giving this cookie to any other empty child would be
            # a symmetrical and redundant computation. So, we can stop
            # after trying this one empty child.
            if distribution[i] == 0:
                break



# class Solution:
#     def distributeCookies(self, cookies: List[int], k: int) -> int:
#         # 76265
#         res = inf

#         # @lru_cache(maxsize=None)
#         def solve(start, v):
#             nonlocal res

#             if start==len(cookies):
#                 res = min(res, max(v))
#                 return

#             for i in range(k):
#                 v[i] += cookies[start]
#                 solve(start+1, v)
#                 v[i] -= cookies[start]

#         solve(0, [0]*k)
        

#         return res