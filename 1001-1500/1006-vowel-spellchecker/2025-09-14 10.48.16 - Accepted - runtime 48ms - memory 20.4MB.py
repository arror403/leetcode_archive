class Solution:
    # claude #
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def normalize_vowels(word):
            return ''.join('@' if c.lower() in 'aeiou' else c.lower() for c in word)
        
        # Build lookup structures
        exact = set(wordlist)
        case_insensitive = {}
        vowel_insensitive = {}
        
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            
            normalized = normalize_vowels(word)
            if normalized not in vowel_insensitive:
                vowel_insensitive[normalized] = word
        
        # Pre-process queries to avoid repeated computations
        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            else:
                lower_query = query.lower()
                if lower_query in case_insensitive:
                    result.append(case_insensitive[lower_query])
                else:
                    normalized_query = normalize_vowels(query)
                    result.append(vowel_insensitive.get(normalized_query, ""))
        
        return result