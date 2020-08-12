import math
import time
import random


# Answer to question One.
def count_comparisons_with_quicksort_first_element_as_pivot(array, start_idx, end_idx): # end_idx is included
    # base case
    if  end_idx - start_idx + 1 <= 1:
        return array, 0
    else:
        # do the partitioning
        pivot = start_idx
        pivot_value = array[start_idx]

        # defining boundaries
        pivot_separating_boundary = start_idx + 1
        partitioned_boundary = start_idx + 1

        # counting_comparisons
        comparisons = end_idx - start_idx + 1 - 1

        while partitioned_boundary <= end_idx:
            if pivot_value < array[partitioned_boundary]:
                partitioned_boundary += 1
            else:
                (array[pivot_separating_boundary], array[partitioned_boundary]) = (array[partitioned_boundary], array[pivot_separating_boundary])
                pivot_separating_boundary += 1
                partitioned_boundary += 1

        # print(array[start_idx: end_idx+ 1])
        # placing pivot at its position
        (array[start_idx], array[pivot_separating_boundary - 1]) = (array[pivot_separating_boundary - 1], array[start_idx])

        # call recursions
        left_partition, left_comparisons = count_comparisons_with_quicksort_first_element_as_pivot(array, start_idx, pivot_separating_boundary - 2)
        right_partition, right_comparisons = count_comparisons_with_quicksort_first_element_as_pivot(array, pivot_separating_boundary, end_idx)

        return array, comparisons + left_comparisons + right_comparisons


def count_comparisons_with_quicksort_final_element_as_pivot(array, start_idx, end_idx): # end_idx is included
    # base case
    if  end_idx - start_idx + 1 <= 1:
        return array, 0
    else:
        # do the partitioning
        (array[start_idx], array[end_idx]) = (array[end_idx], array[start_idx])
        pivot = start_idx
        pivot_value = array[start_idx]

        # defining boundaries
        pivot_separating_boundary = start_idx + 1
        partitioned_boundary = start_idx + 1

        # counting_comparisons
        comparisons = end_idx - start_idx + 1 - 1

        while partitioned_boundary <= end_idx:
            if pivot_value < array[partitioned_boundary]:
                partitioned_boundary += 1
            else:
                (array[pivot_separating_boundary], array[partitioned_boundary]) = (array[partitioned_boundary], array[pivot_separating_boundary])
                pivot_separating_boundary += 1
                partitioned_boundary += 1

        # print(array[start_idx: end_idx+ 1])
        # placing pivot at its position
        (array[start_idx], array[pivot_separating_boundary - 1]) = (array[pivot_separating_boundary - 1], array[start_idx])

        # call recursions
        left_partition, left_comparisons = count_comparisons_with_quicksort_first_element_as_pivot(array, start_idx, pivot_separating_boundary - 2)
        right_partition, right_comparisons = count_comparisons_with_quicksort_first_element_as_pivot(array, pivot_separating_boundary, end_idx)

        return array, comparisons + left_comparisons + right_comparisons



def count_comparisons_with_quicksort_median_element_as_pivot(array, start_idx, end_idx): # end_idx is included
    # base case
    if  end_idx - start_idx + 1 <= 1:
        return array, 0
    else:
        # do the partitioning
        middle_element = math.floor((end_idx - start_idx) / 2.0)
        candidate_pivot_values = [(start_idx, array[start_idx]), (middle_element, array[middle_element]), (end_idx, array[end_idx])]
        sorted_candidates = sorted(candidate_pivot_values, key=lambda x: x[1])

        # swapping pivot value with the start idx
        (array[start_idx], array[sorted_candidates[1][0]]) = (array[sorted_candidates[1][0]], array[start_idx])

        pivot = start_idx
        pivot_value = array[start_idx]

        # defining boundaries
        pivot_separating_boundary = start_idx + 1
        partitioned_boundary = start_idx + 1

        # counting_comparisons
        comparisons = end_idx - start_idx + 1 - 1

        while partitioned_boundary <= end_idx:
            if pivot_value < array[partitioned_boundary]:
                partitioned_boundary += 1
            else:
                (array[pivot_separating_boundary], array[partitioned_boundary]) = (array[partitioned_boundary], array[pivot_separating_boundary])
                pivot_separating_boundary += 1
                partitioned_boundary += 1

        # print(array[start_idx: end_idx+ 1])
        # placing pivot at its position
        (array[start_idx], array[pivot_separating_boundary - 1]) = (array[pivot_separating_boundary - 1], array[start_idx])

        # call recursions
        left_partition, left_comparisons = count_comparisons_with_quicksort_median_element_as_pivot(array, start_idx, pivot_separating_boundary - 2)
        right_partition, right_comparisons = count_comparisons_with_quicksort_median_element_as_pivot(array, pivot_separating_boundary, end_idx)

        return array, comparisons + left_comparisons + right_comparisons


if __name__ == "__main__":
    file_path = "QuickSort.txt"
    with open(file_path) as i:
        input_data = i.readlines()
    input_data = [int(inp.strip()) for inp in input_data]
    print("Total length of the input array is {}.".format(len(input_data)))
    start_time_a = time.time()
    sorted_1, comp1 = count_comparisons_with_quicksort_first_element_as_pivot(input_data.copy(), 0, len(input_data) - 1)
    end_time_a = time.time()
    start_time_b = time.time()
    sorted_2, comp2 = count_comparisons_with_quicksort_final_element_as_pivot(input_data.copy(), 0, len(input_data) - 1)
    end_time_b = time.time()
    start_time_c = time.time()
    sorted_3, comp3 = count_comparisons_with_quicksort_median_element_as_pivot(input_data.copy(), 0, len(input_data) - 1)
    end_time_c = time.time()
    print("Number of total Comparisons by Quicksort with first element as pivot : {}".format(comp1))
    print("Time Required for sorting == {} seconds".format(end_time_a - start_time_a))
    print()
    print("Number of total Comparisons by Quicksort with final element as pivot : {}".format(comp2))
    print("Time Required for sorting == {} seconds".format(end_time_b - start_time_b))
    print()
    print("Number of total Comparisons by Quicksort with median element as pivot : {}".format(comp3))
    print("Time Required for sorting == {} seconds".format(end_time_c - start_time_c))
