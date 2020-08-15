import time
import random
from copy import deepcopy


def randomized_selection(array,  n, statistic_order): # end_idx is included
    """
    Implementation of Randomized Selection of ith order statistic in an unsorted array.
    Args:
        array (list): unsorted array
        n (int) : lenght of the array
        statistic_order (int) : order of the statistics required
    """
    # base case
    if  n <= 1:
        return array[n - 1]
    else:
        # do the partitioning
        pivot = random.randint(0, n - 1)
        # swapping pivot with start_idx
        (array[pivot], array[0]) = (array[0], array[pivot])
        pivot_value = array[0]

        # defining boundaries
        pivot_separating_boundary = 0 + 1
        partitioned_boundary = 0 + 1

        while partitioned_boundary < n:
            if pivot_value < array[partitioned_boundary]:
                partitioned_boundary += 1
            else:
                (array[pivot_separating_boundary], array[partitioned_boundary]) = (array[partitioned_boundary], array[pivot_separating_boundary])
                pivot_separating_boundary += 1
                partitioned_boundary += 1

        # placing pivot at its position
        (array[0], array[pivot_separating_boundary - 1]) = (array[pivot_separating_boundary - 1], array[0])

        # checking if the pivot is = , > or < than the order asked
        if statistic_order - 1 == pivot_separating_boundary - 1:
            return array[pivot_separating_boundary - 1]
        elif statistic_order - 1 > pivot_separating_boundary -1:
            return randomized_selection(array[pivot_separating_boundary :], len(array[pivot_separating_boundary :]), statistic_order - pivot_separating_boundary)
        elif statistic_order - 1 < pivot_separating_boundary - 1:
            return randomized_selection(array[: pivot_separating_boundary - 1], len(array[: pivot_separating_boundary - 1]), statistic_order)



if __name__ == "__main__":
    unsorted_array = [random.randint(1, 10000) for i in range(1000)]
    print("Unsorted array : \n")
    print(unsorted_array)
    statistics_required = 674
    start_time = time.time()
    value = randomized_selection(deepcopy(unsorted_array), len(unsorted_array), statistics_required)
    end_time = time.time()
    print("Algorithm found that {}th value = {} ".format(statistics_required, value))
    print("True value is {}".format(sorted(unsorted_array)[statistics_required - 1]))
    print("Time Required for finding the {}th statistic is {} seconds".format(statistics_required, end_time - start_time))
