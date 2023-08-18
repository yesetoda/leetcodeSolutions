def gcd(n1,n2):
        while n2!=0:
            temp = n1
            n1 = n2
            n2 = temp%n2
        return n1
class Solution:
    

    def countBeautifulPairs( nums: list[int]) -> int:
        lst = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if gcd(nums[i],nums[j]) == 1:
                    lst.append(sorted([nums[i],nums[j]]))
        return lst
    print(countBeautifulPairs(nums = [31,25,72,74,79]))