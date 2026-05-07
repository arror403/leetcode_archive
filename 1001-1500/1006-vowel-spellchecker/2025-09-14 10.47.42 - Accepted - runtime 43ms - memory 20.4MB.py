class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def normalize_vowels(word):
            return ''.join('@' if c.lower() in 'aeiou' else c.lower() for c in word)
        
        # Build lookup structures
        exact = set(wordlist)  # O(1) exact match lookup
        case_insensitive = {}  # lowercase -> first occurrence
        vowel_insensitive = {}  # normalized -> first occurrence
        
        for word in wordlist:
            lower_word = word.lower()
            normalized = normalize_vowels(word)
            
            # Only store first occurrence (maintain priority)
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            if normalized not in vowel_insensitive:
                vowel_insensitive[normalized] = word
        
        # Process queries
        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif normalize_vowels(query) in vowel_insensitive:
                result.append(vowel_insensitive[normalize_vowels(query)])
            else:
                result.append("")
        
        return result