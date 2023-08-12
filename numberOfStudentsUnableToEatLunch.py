# class Solution:
#     def countStudents( students: list[int], sandwiches: list[int]) -> int:
#         count = 0
#         leng = len(students)
#         while count<leng:
#             print(students,sandwiches[::-1],students[0],sandwiches[::-1][0])
#             if sandwiches[-1] == students[0]:
#                 sandwiches.pop()
#                 students.pop(0)
#                 count = 0
#             else:
#                 students.append(students.pop(0))
#                 count+=1
#         return count
#     print(countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
class Solution:
    def countStudents(students, sandwiches):
        count = 0  
        n = len(students) 
        while count < n and students:
            print(students)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0 
            else:
                students.append(students.pop(0))
                count += 1
        return len(students)

print(Solution.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))