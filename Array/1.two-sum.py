from typing import Optional, List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i, key in enumerate(nums):
            dict[key] = i 

        for i in range(len(nums)):
            remain_val = target - nums[i]

            if (remain_val in dict.keys()) and (i != dict[remain_val]):
                return([i, dict[remain_val]])

        return []    

sol = Solution()

#print(sol.twoSum(nums = [2,7,11,15], target = 9))
#print(sol.twoSum(nums = [3,2,4], target = 6))
print(sol.twoSum(nums = [3,3], target = 6))


"""
Since here dict gets updated with duplicate value,
make sure to access the items in dict with nums[i],rather than
iterating through dict. We use this approach as duplicate dict value will
get updated with recent value of dict.

T(n) = O(n)
S(n) = O(n)
"""

        