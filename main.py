from practice.DoublyLinkedList import DoublyLinkedList

def main():
    dll = DoublyLinkedList(1)
    dll.append(0)
    dll.append(3)
    dll.append(2)
    dll.append(4)
    dll.append(5)

    print(dll.swap_pairs())
    print(dll)

if __name__ == '__main__':
    main()