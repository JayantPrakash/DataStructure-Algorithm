from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True

            window.add(nums[R])

        return False

sol = Solution()
nums = [1,2,3,1]
k = 3

nums = [1,0,1,1]
k = 1

nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums,k))            