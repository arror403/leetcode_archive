class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        @lru_cache(None)
        def dfs(num: int, parts: int) -> tuple:
            if parts == 1:
                return (num,)

            min_diff = inf
            best_factors = None

            # Try every divisor i of num
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    quotient = num // i

                    # Recursively factorize quotient into (parts-1) parts
                    remaining_factors = dfs(quotient, parts - 1)

                    if remaining_factors:
                        # Build new factorization including current divisor i
                        current_factors = (i,) + remaining_factors

                        # Sort to easily compute min and max factor
                        sorted_factors = tuple(sorted(current_factors))
                        diff = sorted_factors[-1] - sorted_factors[0]

                        # Keep track of the factorization with the minimum difference
                        if diff < min_diff:
                            min_diff = diff
                            best_factors = sorted_factors

                            # Early stop if perfect split found
                            if min_diff == 0:
                                break

            return best_factors

        return list(dfs(n, k))

        # def partition_list(elements: list, num_parts: int):
  
        #     n = len(elements)

        #     if num_parts <= 0 or num_parts > n:
        #         return

        #     if num_parts == 1:
        #         yield [elements]
        #         return

        #     if num_parts == n:
        #         yield [[e] for e in elements]
        #         return

        #     first_element = elements[0]
        #     rest_of_elements = elements[1:]

        #     for sub_partition in partition_list(rest_of_elements, num_parts - 1):
        #         yield [[first_element]] + sub_partition

        #     for sub_partition in partition_list(rest_of_elements, num_parts):
        #         for i in range(num_parts):
        #             new_partition = sub_partition[:]  # Make a shallow copy of the list of parts
                    
        #             new_partition[i] = [first_element] + new_partition[i]
        #             yield new_partition


        # def primeFactors(num):
        #     factors = []
        #     spf = [0 for i in range(num+1)]
        #     spf[1] = 1
        #     for i in range(2, num+1):
        #         spf[i] = i
        #     for i in range(4, num+1, 2):
        #         spf[i] = 2
        
        #     for i in range(3, int(num**0.5)+1):
        #         if spf[i] == i:
        #             for j in range(i*i, num+1, i):
        #                 if spf[j] == j:
        #                     spf[j] = i
                            
        #     while num != 1:
        #         factors.append(spf[num])
        #         num //= spf[num]

        #     return factors
        

        # p = list(partition_list(primeFactors(n), k))
        # res = [prod(x) for x in p.pop()]
        # D = (max(res) - min(res))
        # for s in p:
        #     t = [prod(x) for x in s]
        #     d = (max(t) - min(t))  
        #     if d < D:
        #         D = d
        #         res = t


        # return res