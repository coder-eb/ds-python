from practice.DoublyLinkedList import DoublyLinkedList

def main():
    dll = DoublyLinkedList(0)
    dll.append(1)
    dll.append(0)

    print(dll.is_palindrome())
    print(dll)

if __name__ == '__main__':
    main()