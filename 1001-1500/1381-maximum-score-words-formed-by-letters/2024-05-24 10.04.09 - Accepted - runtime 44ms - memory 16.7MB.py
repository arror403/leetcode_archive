class Solution:
    ##### power by chatGPT #####
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # t=[sum(score[ord(c)-97] for c in w) for w in words]
        # d=Counter(letters)

        def word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def can_form(word_counter, available_counter):
            return all(word_counter[c] <= available_counter[c] for c in word_counter)
        
        def backtrack(index, available_counter):
            if index == len(words): return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, available_counter)
            
            word_counter = word_counters[index]
            
            # Option 2: Include the current word if possible
            if can_form(word_counter, available_counter):
                new_available_counter = available_counter - word_counter
                score_with_word = word_scores[index] + backtrack(index + 1, new_available_counter)
                max_score = max(max_score, score_with_word)
            
            return max_score
        
        word_counters = [Counter(word) for word in words]
        word_scores = [word_score(word) for word in words]
        available_counter = Counter(letters)
        
        return backtrack(0, available_counter)