from practice.LinkedList import LinkedList

def main():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    # ll.append(2)
    print(ll)
    print(ll.reverse())
    print(ll)
    print(ll.head)
    print(ll.tail)

if __name__ == '__main__':
    main()