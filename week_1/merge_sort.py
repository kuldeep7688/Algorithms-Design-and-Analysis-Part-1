import time
import random


def merge_routine(array_a, array_b):
    """
    Merging routine for two arrays in increasing order.
    Args:
        array_a (list): sorted array
        array_b (list): sorted array
    Returns:
        list: sorted array
    """
    array_a_idx = 0
    array_b_idx = 0
    final_array = [None]*(len(array_a) + len(array_b))
    final_array_idx = 0
    while array_a_idx < len(array_a) and array_b_idx < len(array_b):
        if array_a[array_a_idx] <= array_b[array_b_idx]:
            final_array[final_array_idx] = array_a[array_a_idx]
            array_a_idx += 1
        else:
            final_array[final_array_idx] = array_b[array_b_idx]
            array_b_idx += 1
        final_array_idx += 1

    while array_a_idx < len(array_a):
        final_array[final_array_idx] = array_a[array_a_idx]
        final_array_idx += 1
        array_a_idx += 1

    while array_b_idx < len(array_b):
        final_array[final_array_idx] = array_b[array_b_idx]
        final_array_idx += 1
        array_b_idx += 1
    return final_array


def merge_sort(array):
    """
    Merge Sort implementation.
    Args:
        array (list): unsorted array
    Returns:
        list: sorted array
    """
    if len(array) == 1:
        return array
    else:
        array_a = merge_sort(array[: len(array)//2])
        array_b = merge_sort(array[len(array)//2 :])
        final_array = merge_routine(array_a, array_b)
        return final_array


if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    start_time = time.time()
    sorted_array = merge_sort(unsorted_array)
    end_time = time.time()
    print("Sorted array : \n")
    print(sorted_array)
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
