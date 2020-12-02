# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
#
# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        # Save keys
        keys = {"(": ")",
                "[": "]",
                "{": "}"}
        stack = []
        for i in s:
            if i in dict:
                stack.append(i)
            # Pop if parenthesis matched
            elif len(stack) > 0 and i == keys[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0