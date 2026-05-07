class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        pq = []
        heapify(pq)
        if a: heappush(pq, [-a, 'a'])  # Use negative values for max heap
        if b: heappush(pq, [-b, 'b'])
        if c: heappush(pq, [-c, 'c'])
        
        while pq:
            count, char = heappop(pq)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not pq:
                    break
                count2, char2 = heappop(pq)
                res += char2
                count2 += 1
                if count2 < 0:
                    heappush(pq, [count2, char2])
            else:
                res += char
                count += 1
            
            if count < 0:
                heappush(pq, [count, char])
        
        
        return res

        # d=sorted([('a',a) ,('b',b) ,('c',c)], key=lambda x:x[1], reverse=1)
        # res=""
        # print(d)
        # g=d[0][1]//2+d[0][1]%2
        # g=[x[1]//2+x[1]%2 for x in d]

        # for x in d:

        # return ''