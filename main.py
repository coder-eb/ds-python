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



def main():
    bst = BinarySearchTree()
    bst.insert(47)
    bst.insert(21)
    bst.insert(76)
    bst.insert(18)
    bst.insert(27)
    print(bst.BFS())

if __name__ == "__main__":
    main()
