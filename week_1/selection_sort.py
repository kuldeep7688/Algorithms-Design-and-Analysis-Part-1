import time
import random


def selection_sort(array):
    """
    Implementation of selection sort
    Args:
        array (list): unsorted array

    Returns:
        list: sorted array
    """
    array_sorted_till_idx = 0

    while array_sorted_till_idx < len(array) - 1:
        current_idx = array_sorted_till_idx + 1

        curr_min_idx = array_sorted_till_idx
        while current_idx < len(array):
            if array[curr_min_idx] > array[current_idx]:
                curr_min_idx = current_idx
            current_idx += 1

        (array[array_sorted_till_idx], array[curr_min_idx]) = (array[curr_min_idx], array[array_sorted_till_idx])
        array_sorted_till_idx += 1
    return array


if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    start_time = time.time()
    sorted_array = selection_sort(unsorted_array)
    end_time = time.time()
    print("Sorted array : \n")
    print(sorted_array)
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
