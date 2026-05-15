"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input:
nums=[0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        # Swap non-zero elements with the write pointer position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_index], nums[i] = nums[i], nums[write_index]
                write_index += 1

        return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    result = Solution().moveZeroes(nums)
    print(f"result : {result}")
