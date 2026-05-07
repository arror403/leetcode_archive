class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        sandwiches=deque(sandwiches)
        i=0
        while 1:
            if sandwiches[0]==students[0]:
                i=0
                sandwiches.popleft()
                students.popleft()
                if len(students)==0: return 0
            else:
                students.rotate(-1)
                i+=1

            if i==len(students): 
                return len(students)