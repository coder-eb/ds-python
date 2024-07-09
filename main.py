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
    bst.insert(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(2)
    bst.insert(32)
    print(bst.r_contains(32))



if __name__ == "__main__":
    main()