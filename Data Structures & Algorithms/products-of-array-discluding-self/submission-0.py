class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        prefix = 1

        # left side
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # right side
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer