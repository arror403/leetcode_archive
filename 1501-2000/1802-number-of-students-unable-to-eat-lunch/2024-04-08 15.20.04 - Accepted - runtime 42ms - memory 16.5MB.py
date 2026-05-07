class Solution:
    ##### power by chatGPT #####
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_count = [0, 0]  # Count of students who prefer each type of sandwich
        for student in students:
            students_count[student] += 1
        
        for sandwich in sandwiches:
            if students_count[sandwich] == 0:
                break  # No more students left who prefer this type of sandwich
            students_count[sandwich] -= 1

        return sum(students_count)