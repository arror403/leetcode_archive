class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages=list(map(set, languages))
        dontspeak=set()
        langcount=Counter()

        for u,v in friendships:
            u-=1
            v-=1

            if languages[u]&languages[v]: continue

            dontspeak.add(u)
            dontspeak.add(v)

        for f in dontspeak:
            for l in languages[f]:
                langcount[l]+=1


        return len(dontspeak)-max(langcount.values()) if dontspeak else 0