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
    ll = LinkedList(5)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(1)
    print(find_kth_from_end(ll, 6))

if __name__ == "__main__":
    main()