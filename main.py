from practice.DoublyLinkedList import DoublyLinkedList

def main():
    ll = DoublyLinkedList(0)
    ll.append(1)
    ll.append(2)
    ll.prepend(0)

    print(ll, ll.head, ll.tail)

    ll.pop()
    print(ll, ll.head, ll.tail)
    ll.pop()
    print(ll, ll.head, ll.tail)
    print(ll.pop_first())

if __name__ == '__main__':
    main()