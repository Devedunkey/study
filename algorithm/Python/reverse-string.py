# https://leetcode.com/problems/valid-palindrome/
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Option 1
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)

        start = 0
        end = len(s) - 1

        for i in range(len(s)):
            # Check Valid Palindrome
            if s[start] != s[end]:
                return False

            if start > end:
                break
            start += 1
            end -= 1

        return True

        # Option 2
        # s = s.lower()
        # s = re.sub("[^a-z0-9]", "", s)
        # return s == s[:: -1]


