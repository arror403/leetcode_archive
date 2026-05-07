class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
        # t=0
        # for i in words:
        #     while 1:
        #         x=0
        #         for j in s:
        #             if x<len(i) and i[x]==j: 
        #                 x+=1
        #         if len(i)==x:
        #             t+=1
        #             break
        #         else: 
        #             break
        # return t