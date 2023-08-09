class Solution:
    def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
        count = 0
        for i in hours:
            if i>= target:
                count+=1
        return count
    print(numberOfEmployeesWhoMetTarget( hours = [5,1,4,2,2], target = 6))