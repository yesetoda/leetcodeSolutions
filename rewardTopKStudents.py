# class Solution:
#     def topStudents( positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
#         scoredict = {}
#         for i in range(len(report)):
#             score = 0
#             for j in positive_feedback:
#                 print(j,report[i].count(j))
#                 score+=3*report[i].count(j)
#             for j in negative_feedback:
#                 score-=report[i].count(j)
#             scoredict[student_id[i]] = score
#             print(score)
#         print(scoredict)
        
#         print(sorted(scoredict))
#         print(sorted(scoredict,key = lambda x:scoredict[x]))
#     print(topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart,smart"], student_id = [1,2], k = 2))

# class Solution:
#     def topStudents(positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
#         scoredict = {}
#         for i in range(len(report)):
#             score = 0
#             for j in positive_feedback:
#                 score += 3 * report[i].count(j)
#             for j in negative_feedback:
#                 score -= report[i].count(j)
#             scoredict[student_id[i]] = score
#         sorted_scores = sorted(scoredict.items(), key=lambda x: (-x[1], x[0]))
#         sorted_students = [student[0] for student in sorted_scores]
#         return sorted_students[:k]
#     print(topStudents(positive_feedback =["b","a","b","ba","ab"],negative_feedback =["aa","bb","bb","aa"],report =["a","bbab","aabb","b","aa"],student_id =[4,3,2,5,1],k =5))

from collections import Counter, defaultdict

class Solution:
    def topStudents(positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        positive_counts = Counter(positive_feedback)
        negative_counts = Counter(negative_feedback)
        scoredict = {}

        for i in range(len(report)):
            if student_id[i] in scoredict:
                score = scoredict[student_id[i]]
            else:
                score = 0

            report_counts = Counter(report[i].split())

            for word, count in report_counts.items():
                if word in positive_counts:
                    score += 3 * count * positive_counts[word]
                if word in negative_counts:
                    score -= count * negative_counts[word]

            scoredict[student_id[i]] = score

        sorted_scores = sorted(scoredict.items(), key=lambda x: (-x[1], x[0]))
        sorted_students = [student[0] for student in sorted_scores]

        return sorted_students[:k]

    print(topStudents(positive_feedback =["b","a","b","ba","ab"],negative_feedback =["aa","bb","bb","aa"],report =["a","bbab","aabb","b","aa"],student_id =[4,3,2,5,1],k =5))