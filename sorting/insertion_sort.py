def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1

        # Shift elements greater than key to the right
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        
        # Place key in its correct position
        nums[j+1] = key
    return nums


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before : {nums}")
    insertion_sort(nums)
    print(f"After Insertion Sort : {nums}")
