from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, L = 0, 0
        min_length = float("inf")
        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                min_length = min(R-L+1, min_length)
                total -= nums[L]
                L += 1
    
        if min_length == float("inf"): return 0
        return min_length

sol = Solution()
target = 7
nums = [2,3,1,2,4,3]  

target = 4
nums = [1,4,4]

target = 11
nums = [1,1,1,1,1,1,1,1]
"""
nums = [1,2,3,4,5]
target = 11
"""
print(sol.minSubArrayLen(target, nums))  

"""
T(n) = O(n)
S(n) = O(1)
"""