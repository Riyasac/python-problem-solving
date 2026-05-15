def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i
        
        # Find the actual minimum in the remaining unsorted part
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        
        # Swap only once per iteration
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before : {nums}")
    selection_sort(nums)
    print(f"After Selection Sort : {nums}")
