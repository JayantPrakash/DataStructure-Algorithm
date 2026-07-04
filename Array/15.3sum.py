class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSum(l,r, target):

            while l < r:
                if nums[l] + nums[r] + target == 0:
                    candidate_3sum = [target,nums[l],nums[r]]
                    if candidate_3sum not in ans:
                        ans.append(candidate_3sum)
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
            twoSum(left,right, target)
        return ans

sol = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [0,1,1]
nums = [0,0,0]
print(sol.threeSum(nums))
