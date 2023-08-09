class Solution:
    # def nextGreaterElements(nums: list[int]) -> list[int]:
    #     out= []
    #     i = 0
    #     for _ in range(len(nums)):
    #         print(i)
    #         if i+1==len(nums):
    #             i = 0
    #         j = i+1
    #         while(nums[i]<nums[j]):
    #             j+=1
    #             if i == j:
    #                 out[i] = -1
    #         else:
    #             out[i] == nums[j]
    #         i+=1
    #     return  out
    # print(nextGreaterElements(nums = [1,2,3,4,3]))
    
    # def nextGreaterElements(nums: list[int]) -> list[int]:
    #     length = len(nums)
    #     out = [-1] * length
    #     stack = []

    #     for i in range(2 * length - 1, -1, -1):
    #         while stack and nums[stack[-1]] <= nums[i % length]:
    #             stack.pop()

    #         if stack:
    #             out[i % length] = nums[stack[-1]]
            
    #         stack.append(i % length)

    #     return out
            
    def nextGreaterElements(nums: list[int]) -> list[int]:
        length = len(nums)
        out = [-1] * length
        for i in range(length):
            for j in range(i + 1, i + length + 1):
                if nums[j % length] > nums[i]:
                    out[i] = nums[j % length]
                    break
        return out
        
        # out = []
        # for i in range(len(nums)):
        #     j = i
        #     while True:
        #         if j < len(nums)-1:
        #             j += 1
        #             print("less")
        #         elif j == len(nums)-1:
        #             j = 0
        #             print("equal")
        #         if j == i:
        #             break
        #         print(i, j)
    print(nextGreaterElements(nums = [1,2,1]))