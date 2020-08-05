import time
import random


def bubble_sort(array):
    """
    Bubble Sort Algorithm implementation.
    Args:
        array (list): list of numbers
    Returns:
        list: sorted array
    """
    for swap_till_idx in range(len(array) - 1, 0, -1):
        for i_idx in range(swap_till_idx):
            if array[i_idx] > array[i_idx + 1]:
                array[i_idx], array[i_idx + 1] = array[i_idx + 1], array[i_idx]
    return array


if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    start_time = time.time()
    sorted_array = bubble_sort(unsorted_array)
    end_time = time.time()
    print("Sorted array : \n")
    print(sorted_array)
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
