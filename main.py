from practice.LinkedList import LinkedList

def main():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll)
    print(ll.reverse_between(0, 4))
    print(ll)
    print(ll.head)
    print(ll.tail)

if __name__ == '__main__':
    main()