from practice.DoublyLinkedList import DoublyLinkedList

def main():
    ll = DoublyLinkedList(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print(ll.get(0))

if __name__ == '__main__':
    main()