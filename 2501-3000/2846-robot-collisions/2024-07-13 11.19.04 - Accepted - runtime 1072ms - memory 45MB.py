class Robot:
    def __init__(self, position, health, direction, index):
        self.position = position
        self.health = health
        self.direction = direction
        self.index = index


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack=[]
        vals=[Robot(positions[i], healths[i], directions[i], i) for i in range(len(positions))]

        vals.sort(key=operator.attrgetter('position'))

        for robot in vals:
            if robot.direction=='R':
                stack.append(robot)
                continue
            
            # Check if the robot should be eliminated
            gone=False

            # Process the stack to eliminate robots with lower health
            while stack and stack[-1].health<=robot.health and stack[-1].direction=='R':
                if (stack[-1].health==robot.health):
                    stack.pop()
                    gone=True
                    break

                robot.health-=1
                stack.pop()

            # If the robot is not yet eliminated and there is a robot facing right with higher health
            if (not gone) and stack and stack[-1].direction=='R' and stack[-1].health>robot.health:
                stack[-1].health-=1
                gone=True

            # If the robot is not eliminated, add it to the stack
            if (not gone): stack.append(robot)
    
        stack.sort(key=operator.attrgetter('index'))


        return [robot.health for robot in stack]