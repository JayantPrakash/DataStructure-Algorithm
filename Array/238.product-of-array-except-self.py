from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_arr = len(nums)
        prefix = [1] * len_arr
        suffix = [1] * len_arr
        j = len_arr - 2
        for i in range(1,len_arr):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[j] = suffix[j+1] * nums[j+1]
            j = j - 1

        ans = [1] * len_arr
        for i in range(len_arr):
            ans[i] = prefix[i] * suffix[i]

        return ans     

sol = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))