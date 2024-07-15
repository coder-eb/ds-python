from math import factorial
from DS.BinarySearchTree import BinarySearchTree
from DS.Graph import Graph
from DS.LinkedList import LinkedList
from DS.MaxHeap import MaxHeap
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable
from problems.HT import find_pairs, has_unique_chars, longest_consecutive_sequence, subarray_sum
from problems.MH import find_kth_smallest, stream_max
from problems.random import remove_element

def main():
    bst = BinarySearchTree()
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    bst.sorted_list_to_bst(nums)

if __name__ == "__main__":
    main()