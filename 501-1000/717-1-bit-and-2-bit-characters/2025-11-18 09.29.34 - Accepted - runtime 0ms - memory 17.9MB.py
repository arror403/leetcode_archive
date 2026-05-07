class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)-1
        
        while i < n:
            if bits[i] == 0: 
                i += 1
            else: 
                i += 2


        return i==n



        # def delete_nth(q, n):
        #     q.rotate(-n)
        #     q.popleft()
        #     q.rotate(n)

        # if set(bits)=={0}: return True

        # d = deque(bits)
        # while d:
        #     if d[0]==0:
        #         d.popleft()
        #     else:
        #         break

        # while 1:
        #     f = True
        #     for i in range(len(d)-1):
        #         if d[i]:
        #             delete_nth(d, i)
        #             delete_nth(d, i)
        #             f = False
        #             break
        #         else:
        #             d.popleft()
        #             break
        #     print(f, d)
        #     if f: break

        
        # return set(d)=={0}