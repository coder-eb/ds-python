from math import factorial
from DS.BinarySearchTree import BinarySearchTree, test_invert_tree
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


def fibonacci(n):
    items = [0, 1]
    for i in range(2, n+1):
        new_item = items[-1] + items[-2]
        items.append(new_item)
    return items[n]

def main():
    print(fibonacci(1))

if __name__ == "__main__":
    main()
