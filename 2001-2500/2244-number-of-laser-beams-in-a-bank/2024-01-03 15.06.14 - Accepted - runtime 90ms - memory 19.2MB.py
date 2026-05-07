class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ##### improved by chatGPT #####
        # counts = [w for i in bank if (w:=sum(map(lambda x: x=='1', i)))>0]
        # return sum(counts[x-1]*counts[x] for x in range(1,len(counts))) if len(counts)>1 else 0

        counts = [word.count('1') for word in bank if '1' in word]
        return sum(counts[i-1]*counts[i] for i in range(1,len(counts))) if len(counts)>1 else 0