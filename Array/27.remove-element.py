from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        len_list = len(nums)
        i = 0
        while i < len_list:
            if val == nums[i]:
                nums.pop(i)
                nums.append("_")
            else: 
                if nums[i] != "_":  
                    ans += 1
                i += 1
        nums = nums[0:ans+1]        

        return ans  


sol = Solution()
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))        

"""
T(n) = O(n)
S(n) = O(1)

Here, we should add "_" at the end if val is matched and check if "_" is not there,
when incrementing ans as we unnecssarily inscrease the ans counter
"""