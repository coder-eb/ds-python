from DS.LinkedList import LinkedList
from DS.Stack import Stack
from DS.Queue import Queue
from DS.DoublyLinkedList import DoublyLinkedList

def main():
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(4)
    dll.append(2)
    dll.append(1)
    print(dll.is_palindrome())

if __name__ == "__main__":
    main()