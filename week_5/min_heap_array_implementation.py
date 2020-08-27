import math


# heap with array implementation
class MinHeap(object):
    def __init__(self):
        self.heap_list = []

    def insert(self, item):
        # stick item at the last level
        self.heap_list.append(item)

        # bubble till the heap property is satisfied
        child_idx = len(self.heap_list) - 1
        parent_idx = self.get_parent_idx_given_child_idx(child_idx)

        # heapyifying
        while parent_idx >= 0 and self.heap_list[parent_idx] > self.heap_list[child_idx]:
            (self.heap_list[parent_idx], self.heap_list[child_idx]) = (self.heap_list[child_idx], self.heap_list[parent_idx])
            child_idx = parent_idx
            parent_idx = self.get_parent_idx_given_child_idx(child_idx)
        return

    def get_parent_idx_given_child_idx(self, idx):
        return math.floor((idx - 1) / 2.0)

    def get_children_idxs_give_parent_idx(self, idx):
        return ((2*idx) + 1, (2*idx) + 2)

    def get_smaller_child_idx(self, child_1, child_2):
        if child_2 < len(self.heap_list):
            if self.heap_list[child_1]  < self.heap_list[child_2]:
                return child_1
            else:
                return child_2
        else:
            return child_1

    def extract_min(self):
        min_item = self.heap_list[0]
        if len(self.heap_list) == 1:
            self.heap_list = []
        else:
            self.heap_list[0] = self.heap_list[-1]
            self.heap_list = self.heap_list[:-1]

        parent_idx = 0
        (children_idx_1, children_idx_2) = self.get_children_idxs_give_parent_idx(parent_idx)
        smaller_children_idx = self.get_smaller_child_idx(children_idx_1, children_idx_2)

        while smaller_children_idx < len(self.heap_list) and self.heap_list[smaller_children_idx] < self.heap_list[parent_idx]:
            (self.heap_list[parent_idx], self.heap_list[smaller_children_idx]) = (self.heap_list[smaller_children_idx], self.heap_list[parent_idx])
            parent_idx = smaller_children_idx
            (children_idx_1, children_idx_2) = self.get_children_idxs_give_parent_idx(parent_idx)
            smaller_children_idx = self.get_smaller_child_idx(children_idx_1, children_idx_2)
        return min_item


if __name__ == "__main__":
    keys_to_be_inserted = [15, 5, 3, 17, 10, 84, 19, 6, 22, 9]
    min_heap = MinHeap()

    # inserting keys in heap
    for i in keys_to_be_inserted:
        min_heap.insert(i)
        print(min_heap.heap_list)
        print()

    # extracting min from the heap
    for i in range(len(min_heap.heap_list)):
        print(min_heap.extract_min())
