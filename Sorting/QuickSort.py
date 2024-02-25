from typing import List


def quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", my_list)
quick_sort(my_list, 0, len(my_list) - 1)
print("Sorted array:", my_list)

"""
Time complexity: O(N*log(N)) in the average case, O(N^2) in the worst case
Space complexity: O(log(N))
"""