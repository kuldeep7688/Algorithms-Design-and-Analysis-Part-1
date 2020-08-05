import time
import random


def insertion_sort(array):
    """
    Implementation of insertion sort algorithm.
    Args:
        array (list): unsorted list of numbers

    Returns:
        list: sorted list
    """
    for insertion_idx  in range(1, len(array)):
        value = array[insertion_idx]

        j = insertion_idx
        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1
        array[j] = value
    return array


if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    start_time = time.time()
    sorted_array = insertion_sort(unsorted_array)
    end_time = time.time()
    print("Sorted array : \n")
    print(sorted_array)
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
