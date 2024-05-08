from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

def main():
    my_dll = DoublyLinkedList(0)
    my_dll.append(1)
    my_dll.append(2)
    print(my_dll)
    print(my_dll.get(3))

if __name__ == "__main__":
    main()