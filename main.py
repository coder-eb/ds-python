from DS.LinkedList import LinkedList

def main():
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    print(my_linked_list)
    print(my_linked_list.get(my_linked_list.length-1))

if __name__ == "__main__":
    main()