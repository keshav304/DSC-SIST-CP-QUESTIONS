# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        l = len(nums)
        for i in range(l):
            if (target - nums[i]) in mapp.keys():
                return [mapp[(target - nums[i])], i]
            else:
                mapp[nums[i]] = i

