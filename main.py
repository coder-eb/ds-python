from codecs import namereplace_errors
from DS.BinarySearchTree import BinarySearchTree
from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList
from DS.HashTable import HashTable

def find_kth_from_end(ll: LinkedList, k):
    slow = fast = ll.head
    for iter in range(k):
        if fast == None:
            return None
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow

def item_in_common(list1, list2):
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for item in list2:
        if item in my_dict:
            return True
        
    return False

def main():
    print(item_in_common([1], [1]))
    
if __name__ == "__main__":
    main()