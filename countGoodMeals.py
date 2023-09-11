def is_power_of_two(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0
from random import randint
class Solution:
    def countPairs( deliciousness: list[int]) -> int:
        goodmeals = 0
        for i in range(len(deliciousness)):
            for j in range(i+1,len(deliciousness)):
                if is_power_of_two(deliciousness[i]+deliciousness[j]):
                    goodmeals+=1
        return goodmeals
    print(countPairs([1,1,1,3,3,3,7]))
    print([randint(0,2**20) for i in range(10**4+100)] )
