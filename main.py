from math import factorial
from DS.BinarySearchTree import BinarySearchTree
from DS.Graph import Graph
from DS.LinkedList import LinkedList
from DS.MaxHeap import MaxHeap
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable
from helpers import timeit
from problems.HT import (
    find_pairs,
    has_unique_chars,
    longest_consecutive_sequence,
    subarray_sum,
)
from problems.MH import find_kth_smallest, stream_max
from problems.random import remove_element


def populate_slow_bst(bst: BinarySearchTree, length):
    for number in range(0, length + 1):
        bst.insert(number)


def populate_fast_bst(bst: BinarySearchTree, length):
    numbers = list(range(0, length + 1))
    bst.sorted_list_to_bst(numbers)


@timeit
def check_bst_performance(bst: BinarySearchTree, value):
    is_exists = bst.contains(value)
    print(f"BST contains value: {value} - {is_exists}")


def test_balanced_bst():
    slow_bst = BinarySearchTree()
    fast_bst = BinarySearchTree()
    NO_OF_ELEMENTS = 90_000

    populate_slow_bst(slow_bst, NO_OF_ELEMENTS)
    populate_slow_bst(fast_bst, NO_OF_ELEMENTS)

    check_bst_performance(slow_bst, 1_00_000)
    check_bst_performance(fast_bst, 1_00_000)


def main():
    test_balanced_bst()


if __name__ == "__main__":
    main()
