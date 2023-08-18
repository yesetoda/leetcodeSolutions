from time import perf_counter
class Solution:
    def search(nums: list[int], target: int) -> int:
        # start = 0
        # end = len(nums)-1
        # mid  = (start+end)//2
        # while start!= end:
        # # for i in range(len(nums)):
        #     print(start,end,mid,nums[mid])
        #     if target > nums[mid]:
        #         start = mid
        #         mid = (start+end)//2
        #     elif target < nums[mid]:
        #         end = mid
        #         mid = (start+end)//2
        #     else:
        #         return mid
        # return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    a = perf_counter()
    print(search([-1,0,3,5,9,12], target = 9))
    b = perf_counter()
    print(b-a)