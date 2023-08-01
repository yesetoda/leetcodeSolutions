class Solution:
    def minMovesToSeat(seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            if seats[i] < students[i]:
                moves+= students[i] -seats[i]
            elif seats[i] > students[i]:
                moves+= seats[i] - students[i]
        return moves
    print(minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6]))