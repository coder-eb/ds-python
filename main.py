from DS.BinarySearchTree import BinarySearchTree
from DS.Graph import Graph
from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable
from problems.HT import find_pairs, has_unique_chars, longest_consecutive_sequence, subarray_sum

def main():
    graph = Graph() 
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A','B')
    print(graph)
    graph.remove_edge('A','B')
    graph.remove_edge('A','C')
    print(graph)
    
if __name__ == "__main__":
    main()