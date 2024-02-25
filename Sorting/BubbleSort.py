from typing import List


def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", my_list)
bubble_sort(my_list)
print("Sorted array:", my_list)

"""
Time complexity: O(N^2)
Space complexity: O(1)
"""