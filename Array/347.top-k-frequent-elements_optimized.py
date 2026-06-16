from typing import Optional, List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_elem = {}

        for i in range(len(nums)):
            if nums[i] in dict_elem:
                dict_elem[nums[i]] = dict_elem[nums[i]] + 1
            else:
                dict_elem[nums[i]] = 1

        h = []
        for key, val in dict_elem.items():
            heapq.heappush(h, (val,key))

            if len(h) > k:
                heapq.heappop(h)

        #for i in range(len(h)):
        #    print(h[i])

        result = [heapq.heappop(h)[1] for i in range(k)]        
        return result  


sol = Solution()

print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent( nums = [1], k = 1))
print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))

"""
T(n) = O(nlog(k))
S(n) = O(n+k) # size of heap and dict

Algorithm
Build a frequency map that counts how many times each number appears.
Create an empty min-heap.
For each number in the frequency map:
Push (frequency, number) into the heap.
If the heap size becomes greater than k, pop once to remove the smallest frequency.
After processing all numbers, the heap contains the k most frequent elements.
Pop all elements from the heap and collect their numbers into the result list.
Return the result.

"""
