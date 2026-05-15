def linear_search(data, target):
    print(f"Searching for {target} in the list...")

    for i in range(len(data)):
        print(f"checking item at index {i}: {data[i]}")
        if data[i] == target:
            print("Target found!")
            return i
    print("Target not found.")
    return -1    

if __name__ == "__main__":
    my_list = [5, 12, 8, 23, 16, 2, 38]
    target = 16
    print(f"Index : {linear_search(my_list, target)}")