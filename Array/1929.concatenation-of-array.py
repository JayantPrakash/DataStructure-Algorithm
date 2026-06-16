from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        len_nums = len(nums)
        ans = [0] * 2 * len_nums
        j = 0

        for i in range(len(ans)):
            if len_nums > i:
                ans[i] = nums[i]
            else:
                ans[j + len_nums] = nums[j]
                j += 1    

        return ans     
    
sol = Solution()
print(sol.getConcatenation(nums = [1,2,1]))   

"""
T(n) = O(n)
S(n) = O(n)
"""

        