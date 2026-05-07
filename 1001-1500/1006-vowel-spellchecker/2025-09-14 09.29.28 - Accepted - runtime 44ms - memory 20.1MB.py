class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # wordlist = ["KiTe","kite","hare","Hare"]
        # ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
        # ["kite","KiTe","KiTe","Hare","hare",""    ,""    ,"KiTe",""    ,"KiTe"]

        # re.sub(pattern, repl, string, count=0, flags=0)

        words = {w:w for w in wordlist}
        cap = {w.lower():w for w in wordlist[::-1]}
        vowels = {re.sub('[aeiou]', '@', w.lower()): w for w in wordlist[::-1]}

        print(cap, vowels)

        return [words.get(w) # exactly matches
                or cap.get(w.lower()) # matches a word up to capitlization, return 1st in the wordlist
                or vowels.get(re.sub('[aeiou]', '@', w.lower()), "") # vowel errors, "" for no match
                for w in queries]