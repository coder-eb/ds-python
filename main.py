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
from DS.ListStack import ListStack as Stack

def sort_stack(random_stack: Stack):
    sorted_stack = Stack()
    while not random_stack.is_empty():
        current_num = random_stack.pop()
        
        if sorted_stack.is_empty() or sorted_stack.peek() <= current_num:
            sorted_stack.push(current_num)
        else:
            while not sorted_stack.is_empty() and sorted_stack.peek() > current_num:
                random_stack.push(sorted_stack.pop())
            sorted_stack.push(current_num)
    return sorted_stack

def fibonacci(n):
    items = [0, 1]
    for i in range(2, n+1):
        new_item = items[-1] + items[-2]
        items.append(new_item)
    return items[n]

def main():
    random_stack = Stack()
    random_stack.push(2)
    random_stack.push(4)
    random_stack.push(5)
    random_stack.push(1)
    random_stack.push(3)
    sorted_stack = sort_stack(random_stack)
    print(sorted_stack)

if __name__ == "__main__":
    main()
