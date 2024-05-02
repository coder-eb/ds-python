from DS.LinkedList import LinkedList

def main():
    my_linked_list = LinkedList(5)
    my_linked_list.pop()
    my_linked_list.prepend(6)
    my_linked_list.append(7)
    print(my_linked_list)

if __name__ == "__main__":
    main()