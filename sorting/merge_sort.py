def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    # Divide: into two halves
    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    # Conquer: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine: Merge two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0
    
    # compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before : {nums}")
    nums = merge_sort(nums)
    print(f"After Merge Sort : {nums}")
