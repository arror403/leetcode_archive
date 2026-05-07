class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        helper=lambda x: ''.join(['@' if c in 'aeiouAEIOU' else c.lower() for c in x])

        res=[]
        cap={w.lower():w for w in wordlist[::-1]}
        vowels={helper(w):w for w in wordlist[::-1]}

        for w in queries:
            if w in wordlist:
                res.append(w)
            elif w.lower() in cap:
                res.append(cap[w.lower()])
            else:
                res.append(vowels.get(helper(w), ""))


        return res