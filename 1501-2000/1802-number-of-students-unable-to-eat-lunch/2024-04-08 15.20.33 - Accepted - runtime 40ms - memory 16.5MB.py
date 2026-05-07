class Solution:
    ##### power by chatGPT #####
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        i = 0
        while sandwiches and i < len(students):
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
                i = 0  # Reset the counter since a match was found
            else:
                students.append(students.popleft())  # Rotate the students queue
                i += 1

        return len(sandwiches)