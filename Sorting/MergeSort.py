from typing import List


def merge_sort(arr: List[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2

        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", my_list)
merge_sort(my_list)
print("Sorted array:", my_list)

"""
Time complexity: O(N*log(N))
Space complexity: not fixed
"""