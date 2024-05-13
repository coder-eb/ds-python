from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

def main():
    ll = LinkedList(0)
    # ll.append(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    print(ll.find_middle_node())

if __name__ == "__main__":
    main()