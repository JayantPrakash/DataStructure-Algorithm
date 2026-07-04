"""
Question:
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_str = "".join(char.lower() for char in s if char.isalnum())
        
        l = 0
        r = len(cleaned_str) - 1

        while l < r:
            if cleaned_str[l] != cleaned_str[r]:
                return False
            
            l+=1
            r-=1

        return True
    

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
sol = Solution()
print(sol.isPalindrome(s))