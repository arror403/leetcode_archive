class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        return sorted(Counter(map(int,str(n))).items(), key=lambda x:(x[1],x[0]))[0][0]