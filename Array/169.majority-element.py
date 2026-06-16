from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] = dict[nums[i]] + 1

            if dict[nums[i]] >  int(n/2):
                return nums[i]

sol = Solution()
print(sol.majorityElement(nums = [3,2,3]))
"""
T(n) = O(n)
S(n) = O(n)

Here, the edge case is when max no of majority element is 1, so check if it max for case
when majority element frequency is 1
"""
 


        