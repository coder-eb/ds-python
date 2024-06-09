from DS.BinarySearchTree import BinarySearchTree
from DS.Graph import Graph
from DS.LinkedList import LinkedList
from DS.MaxHeap import MaxHeap
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable
from problems.HT import find_pairs, has_unique_chars, longest_consecutive_sequence, subarray_sum

def main():
    heap = MaxHeap([99, 72, 61, 58])
    heap.insert(100)
    heap.insert(75)
    print(heap.remove())
    print(heap)

if __name__ == "__main__":
    main()