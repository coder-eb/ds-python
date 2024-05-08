from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

def main():
    my_dll = DoublyLinkedList(0)
    my_dll.append(1)
    my_dll.append(2)
    my_dll.append(3)
    print(my_dll)
    print(my_dll.remove(1))
    print(my_dll)

if __name__ == "__main__":
    main()