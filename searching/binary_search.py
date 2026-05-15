def binary_search(data, target):
    print(f"Searching for {target} in the list...")
    
    left = 0
    right = len(data)-1
    while left <= right:
        mid = (left+right)//2        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1    

if __name__ == "__main__":
    my_list = [5, 12, 8, 23, 16, 2, 38]
    my_list = sorted(my_list)
    target = 16
    print(f"Index : {binary_search(my_list, target)}")
