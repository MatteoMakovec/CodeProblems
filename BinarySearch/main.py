def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_list = [11, 12, 22, 25, 34, 64, 90]
target_value = 25

result = binary_search(sorted_list, target_value)

if result != -1:
    print("My array: ", sorted_list)
    print(f"Element {target_value} is present at index {result}.")
else:
    print(f"Element {target_value} is not present in the list.")

"""
Time complexity: O(log(N))
Space complexity: O(1)
"""