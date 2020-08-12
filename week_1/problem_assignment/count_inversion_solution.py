import time
import math
import random

def count_inversion_routine(array_a, array_b):
    """
    Count split inversions and merge arrays routine.
    Args:
        array_a (list): sorted array
        array_b (list): sorted array
    Returns:
        list, count : sorted merged list, count of split inversion
    """
    array_a_idx = 0
    array_b_idx = 0

    final_array = [None]*(len(array_a) + len(array_b))
    final_array_idx = 0
    total_split_inversions = 0

    while array_a_idx < len(array_a) and array_b_idx < len(array_b):
        if array_a[array_a_idx] <= array_b[array_b_idx]:
            final_array[final_array_idx] = array_a[array_a_idx]
            final_array_idx += 1
            array_a_idx += 1
        else:
            final_array[final_array_idx] = array_b[array_b_idx]
            total_split_inversions += len(array_a) - 1 - array_a_idx + 1
            final_array_idx += 1
            array_b_idx += 1

    # if left items in array_b
    while array_b_idx < len(array_b):
        final_array[final_array_idx] = array_b[array_b_idx]
        final_array_idx += 1
        array_b_idx += 1

    # if left items in array_a
    while array_a_idx < len(array_a):
        final_array[final_array_idx] = array_a[array_a_idx]
        final_array_idx += 1
        array_a_idx += 1

    return final_array, total_split_inversions


def count_inversions(array):
    """
    Implementation of count inversions using merge sort algorithm.
    Args:
        array (list): array

    Returns:
        list, int: sorted array, count of total inversion
    """
    if len(array) == 1:
        return array, 0
    else:
        array_a, left_inversions = count_inversions(array[: len(array) // 2])
        array_b, right_inversions = count_inversions(array[len(array) // 2: ])
        merged_array, split_inversions = count_inversion_routine(array_a, array_b)
        return merged_array, left_inversions + right_inversions + split_inversions


if __name__ == "__main__":
    file_path = "IntegerArray.txt"
    with open(file_path) as i:
        input_data = i.readlines()
    input_data = [int(inp.strip()) for inp in input_data]
    print("Total length of the input array is {}.".format(len(input_data)))
    start_time = time.time()
    sorted_array, num_of_inversions = count_inversions(input_data)
    end_time = time.time()
    print("Number of total inversions are : {}".format(num_of_inversions))
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
