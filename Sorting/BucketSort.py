from typing import List


def bucket_sort(arr: List[int]) -> List[int]:
    max_val = max(arr)
    min_val = min(arr)

    bucket_range = (max_val - min_val) / len(arr)
    bucket_list = [[] for _ in range(len(arr) + 1)]

    for value in arr:
        index = int((value - min_val) / bucket_range)
        bucket_list[index].append(value)

    sorted_list = []
    for bucket in bucket_list:
        sorted_list.extend(sorted(bucket))

    return sorted_list


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Array: ", my_list)
my_list = bucket_sort(my_list)
print("Sorted array:", my_list)
