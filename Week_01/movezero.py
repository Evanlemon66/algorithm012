class Solution:
    def moveZeroes(self, nums):
        sgdzzy = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[sgdzzy] = nums[sgdzzy], nums[i]
                sgdzzy += 1