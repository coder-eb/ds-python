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

def main():
    ht = HashTable()
    ht.set_item('bolts', 20)
    ht.set_item('washers', 30)
    ht.set_item('nuts', 10)
    print(ht)
    print(ht.get_item('nuts'))
    print(ht.get_item('washer'))
    print(ht.keys())
    
if __name__ == "__main__":
    main()