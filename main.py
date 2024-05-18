from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

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
    dl = DoublyLinkedList(1)
    dl.append(2)
    dl.append(3)
    dl.append(4)
    dl.append(5)
    dl.append(6)
    dl.swap_pairs()
    print(dl)
     
if __name__ == "__main__":
    main()