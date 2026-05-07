class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res=[]

        w=list(set(words))
        word_count=[]
        for i in w:
            tmp=[i,words.count(i)]
            word_count.append(tmp)

        word_count.sort(key=lambda row: (row[0]), reverse=False)
        word_count.sort(key=lambda row: (row[1]), reverse=True)

        for i in range(k):
            res.append(word_count[i][0])
            
        return res