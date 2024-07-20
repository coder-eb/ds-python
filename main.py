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
    ll = LinkedList(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)
    ll.bubble_sort()
    print(ll)

if __name__ == "__main__":
    main()
