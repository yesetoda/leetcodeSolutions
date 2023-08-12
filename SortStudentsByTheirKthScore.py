class Solution:
    def sortTheStudents( score: list[list[int]], k: int) -> list[list[int]]:
        to_print = []
        diction = {}
        for i,j in enumerate(score):
            diction[j[k]] = j
        out = reversed(sorted(list(diction.keys())))
        # out.sort(reverse = True)
        for i in out:
            to_print.append(diction[i])
        return to_print
    print(sortTheStudents(score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2))