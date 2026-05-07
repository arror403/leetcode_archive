class Solution:
    def countCharacters(self, words: List[str], d: str) -> int:
        
        ##### power by chatGPT #####
        
        d=Counter(d)
        d_keys_set = set(d.keys())
        word_counters = [Counter(word) for word in words]
        
        return sum([len(word) for word_counter, word in zip(word_counters, words) if all([(c in d_keys_set and f <= d[c]) for c, f in word_counter.items()])])