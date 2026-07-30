class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = str(x)[::-1]
        if str(x) == rev_x:
            return True
        else:
            return False