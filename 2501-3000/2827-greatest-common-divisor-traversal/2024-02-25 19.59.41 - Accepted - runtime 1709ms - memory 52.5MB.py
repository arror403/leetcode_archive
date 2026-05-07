class UnionFind:

    def __init__(self, size):
        self.parents=list(range(size))
        self.sizes=[1]*size


    def find(self, node):
        # Recursively find the root of the node and perform path compression
        if self.parents[node]!=node:
            self.parents[node]=self.find(self.parents[node])

        return self.parents[node]


    def union(self, node_a, node_b):
        # Merge the groups containing node_a and node_b
        root_a, root_b = self.find(node_a), self.find(node_b)
        if root_a == root_b:
            return False  # Already in the same set

        # Union by size: attach the smaller tree to the root of the larger tree
        if self.sizes[root_a] > self.sizes[root_b]:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]

        return True


# Max value to be considered for factoring the numbers
max_value = 100010

# Dictionary to hold prime factors for each number
prime_factors = defaultdict(list)

# Pre-calculate prime factors for all numbers up to max_value
for n in range(1, max_value+1):
    v=n
    factor=2
    while factor<=v//factor:
        if v%factor==0:
            prime_factors[n].append(factor)
            while v%factor==0:
                v//=factor
        factor+=1
    if v>1:
        prime_factors[n].append(v)


class Solution:
    def canTraverseAllPairs(self, nums):
        count = len(nums)
        max_num = max(nums)

        # Create a UnionFind instance
        uf = UnionFind(count + max_num + 1)

        # Union numbers with their prime factors
        for i,v in enumerate(nums):
            for prime in prime_factors[v]:
                uf.union(i, prime + count)

        # Check if all numbers are connected (in the same set)
        root_set = {uf.find(i) for i in range(count)}

        return len(root_set) == 1