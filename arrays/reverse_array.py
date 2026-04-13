"""
Reverse an Array (In-Place)

Given an array of integers `nums`, reverse the array in-place.

You must modify the input array directly without using extra space.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

Example 1:
Input: nums = [1,2,3,4,5,6,7]
Output: [7,6,5,4,3,2,1]

Example 2:
Input: nums = [1,2]
Output: [2,1]

Requirements:
- Do not create a new array
- Use O(1) extra space
- Time complexity should be O(n)

Approach:
Use two pointers:
- One starting from the beginning
- One from the end
Swap elements until they meet in the middle
"""

class Solution(object):
    def reverse(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)//2):
            nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
        print(nums)
        return nums

def main():
    nums = [1,2,3,4,5,6,7]
    Solution().reverse(nums)

if __name__ == "__main__":
    main()
