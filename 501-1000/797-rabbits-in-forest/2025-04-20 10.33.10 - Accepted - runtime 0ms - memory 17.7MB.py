class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(ceil(f/(v+1))*(v+1) for v,f in Counter(answers).items())