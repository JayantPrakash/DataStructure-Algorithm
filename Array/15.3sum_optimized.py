from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(l,r, target):

            while l < r:
                if nums[l] + nums[r] + target == 0:
                    ans.append([target,nums[l],nums[r]])
                    l += 1  
                    r -= 1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
                if nums[l] + nums[r] + target < 0:
                    l += 1
                if nums[l] + nums[r] + target > 0:
                    r -= 1

            return 
        
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(left,right, target)
        return ans