class Solution:
    def is_alpha(self, c):
        return (
            ord(c) >= ord('a') and ord(c) < ord('z') or
            ord(c) >= ord('A') and ord(c) < ord('Z') or
            ord(c) >= ord('0') and ord(c) <= ord('9')
        )

    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alpha(s[left]):
                left += 1

            while right > left and not self.is_alpha(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            right -= 1
            left += 1

        return True
        