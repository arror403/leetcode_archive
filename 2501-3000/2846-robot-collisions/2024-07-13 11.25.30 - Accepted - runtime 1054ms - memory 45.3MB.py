##### improved by ChatGPT #####
class Robot:
    def __init__(self, p, h, d, i):
        self.position = p
        self.health = h
        self.direction = d
        self.index = i

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [Robot(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        robots.sort(key=lambda x: x.position)
        
        stack=deque()
        
        for robot in robots:
            if robot.direction=='R':
                stack.append(robot)
            else:
                while stack and stack[-1].direction == 'R':
                    if stack[-1].health == robot.health:
                        stack.pop()
                        break
                    elif stack[-1].health > robot.health:
                        stack[-1].health -= 1
                        break
                    else:
                        robot.health -= 1
                        stack.pop()
                else:
                    stack.append(robot)
        
        stack = sorted(stack, key=lambda x: x.index)


        return [robot.health for robot in stack]