import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = s.lower()
        new_s = re.sub("[^a-z0-9]", "", new_s)

        start = 0
        end = len(new_s) - 1

        for i in range(len(new_s)):
            # Check Valid Palindrome
            if new_s[start] != new_s[end]:
                return False

            if start > end:
                break
            start += 1
            end -= 1

        return True