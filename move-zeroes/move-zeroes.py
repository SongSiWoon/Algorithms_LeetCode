class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cnt = 0
        for i in range(length):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
        nums[cnt:] = [0]*(length - cnt)