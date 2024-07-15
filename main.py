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
    bst.r_insert(10)
    bst.r_insert(9)
    bst.r_insert(2)
    bst.r_insert(5)
    bst.r_insert(6)
    bst.delete_node(9)

if __name__ == "__main__":
    main()