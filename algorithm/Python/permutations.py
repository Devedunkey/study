# https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution(object):
    def permute(self, nums):
        result = []
        prv = []
        def dfs_util(list = []):
            if len(list) == 0:
                result.append(prv[:])
            else:
                for e in list:
                    prv.append(e)
                    nxt = list[:]
                    nxt.remove(e)
                    dfs_util(nxt)
                    prv.pop()
            return result
        return dfs_util(nums)