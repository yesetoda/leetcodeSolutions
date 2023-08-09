class Solution:
    def containsNearbyDuplicate( nums: list[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])

        return False

    print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
                
                
        