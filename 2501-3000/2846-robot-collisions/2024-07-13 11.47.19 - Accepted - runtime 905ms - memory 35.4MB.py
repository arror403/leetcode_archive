class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        left,right=[],[]
        for i in sorted(range(len(positions)), key=lambda i: positions[i]):
            if directions[i]=='R': right.append(i)
            else:
                while right and healths[right[-1]]<healths[i]:
                    right.pop()
                    healths[i]-=1
                if not right: left.append(i)
                elif healths[right[-1]]==healths[i]: right.pop()
                else: healths[right[-1]]-=1
        return [healths[i] for i in sorted(left+right)]


# class Robot:
#     def __init__(self, p, h, d, i):
#         self.position = p
#         self.health = h
#         self.direction = d
#         self.index = i


# class Solution:
#     def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
#         stack=deque()
#         robots=[Robot(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
#         robots.sort(key=lambda x: x.position)

#         for robot in robots:
#             if robot.direction=='R':
#                 stack.append(robot)
#             else:
#                 while stack and stack[-1].direction=='R':
#                     if stack[-1].health==robot.health:
#                         stack.pop()
#                         break
#                     elif stack[-1].health>robot.health:
#                         stack[-1].health-=1
#                         break
#                     else:
#                         robot.health-=1
#                         stack.pop()
#                 else:
#                     stack.append(robot)
        

#         return [r.health for r in sorted(stack, key=lambda x: x.index)]