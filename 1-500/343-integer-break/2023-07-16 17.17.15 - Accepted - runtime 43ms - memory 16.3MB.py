class Solution:
    def integerBreak(self, n: int) -> int:
        # Special cases where n = 2 or n = 3
        if n == 2:
            return 1
        elif n == 3:
            return 2

        # Initialize a list to store the maximum products for each value from 0 to n
        products = [0] * (n + 1)

        # Base cases
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        # Fill the products list using dynamic programming
        for i in range(4, n + 1):
            max_product = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i - j]
                if product > max_product:
                    max_product = product
            products[i] = max_product

        return products[n]