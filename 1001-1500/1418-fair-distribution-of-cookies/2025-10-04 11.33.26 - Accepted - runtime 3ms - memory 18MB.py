class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = inf
        distribution = [0] * k
        
        cookies.sort(reverse=True)

        self.solver(0, distribution, cookies, k)

        return self.res


    def solver(self, cookie_idx, distribution, cookies, k):
        if cookie_idx == len(cookies):
            self.res = min(self.res, max(distribution))
            return

        if max(distribution) >= self.res:
            return

        for i in range(k):
            distribution[i] += cookies[cookie_idx]
            self.solver(cookie_idx + 1, distribution, cookies, k)
            distribution[i] -= cookies[cookie_idx]
            
            if distribution[i] == 0: break