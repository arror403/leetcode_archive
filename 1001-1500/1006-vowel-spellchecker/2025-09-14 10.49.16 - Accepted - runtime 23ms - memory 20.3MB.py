class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def case_hash(s):
            return s.lower()
        
        def vowel_hash(s):
            return s.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
        
        
        exact = set(wordlist)
        case = defaultdict()
        vowl = defaultdict()
        for w in wordlist:
            c = case_hash(w)
            if c not in case: case[c] = w
            v = vowel_hash(w)
            if v not in vowl: vowl[v] = w
        
        def correct(w):
            if w in exact: return w
            c = case_hash(w)
            if c in case: return case[c]
            v = vowel_hash(w)
            if v in vowl: return vowl[v]
            return ''
                    
                    
        return [correct(q) for q in queries]