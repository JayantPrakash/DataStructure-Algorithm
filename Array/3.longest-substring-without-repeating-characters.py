class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        max_len = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R]) 
            max_len = max(len(window), max_len)

        return max_len        
    

sol = Solution()
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))    