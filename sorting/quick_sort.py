def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before : {nums}")
    nums = quick_sort(nums)
    print(f"After Quick Sort : {nums}")
