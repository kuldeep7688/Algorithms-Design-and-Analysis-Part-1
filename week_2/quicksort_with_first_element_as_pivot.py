import time
import random


def quicksort_with_first_element_as_pivot(array, start_idx, end_idx): # end_idx is included
    """
    Implementation of Quicksort with taking first element as the pivot always.
    Args:
        array (list): unsorted array
        start_idx (int) : starting index of the array
        end_idx (int) : end index of the array
    Returns:
        list : sorted array
    """
    # base case
    if  end_idx - start_idx + 1 <= 1:
        return array
    else:
        # do the partitioning
        pivot = start_idx
        pivot_value = array[start_idx]

        # defining boundaries
        pivot_separating_boundary = start_idx + 1
        partitioned_boundary = start_idx + 1

        while partitioned_boundary <= end_idx:
            if pivot_value < array[partitioned_boundary]:
                partitioned_boundary += 1
            else:
                (array[pivot_separating_boundary], array[partitioned_boundary]) = (array[partitioned_boundary], array[pivot_separating_boundary])
                pivot_separating_boundary += 1
                partitioned_boundary += 1

        # placing pivot at its position
        (array[start_idx], array[pivot_separating_boundary - 1]) = (array[pivot_separating_boundary - 1], array[start_idx])

        # call recursions
        left_partition = quicksort_with_first_element_as_pivot(array, start_idx, pivot_separating_boundary - 2)
        right_partition = quicksort_with_first_element_as_pivot(array, pivot_separating_boundary, end_idx)

        return array


if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    start_time = time.time()
    sorted_array = quicksort_with_first_element_as_pivot(unsorted_array, 0, len(unsorted_array) - 1)
    end_time = time.time()
    print("Sorted array : \n")
    print(sorted_array)
    print("Time Required for sorting == {} seconds".format(end_time - start_time))
