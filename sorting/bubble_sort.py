def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before : {nums}")
    bubble_sort(nums)
    print(f"After Bubble Sort : {nums}")
