class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        l = len(nums)
        for i in range(l):
            if (target - nums[i]) in mapp.keys():
                return [mapp[(target - nums[i])], i]
            else:
                mapp[nums[i]] = i


print(Solution.twoSum([-3, 4, 3, 90], 0))
