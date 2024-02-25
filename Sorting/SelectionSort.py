from typing import List


def selection_sort(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", my_list)
selection_sort(my_list)
print("Sorted array:", my_list)

"""
Time complexity: O(N^2)
Space complexity: O(1)
"""