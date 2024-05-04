from DS.LinkedList import LinkedList
from DS.Stack import Stack

def main():
    my_stack = Stack(0)
    my_stack.push(1)
    print(my_stack)
    my_stack.pop()
    print(my_stack)
    my_stack.pop()
    print(my_stack)

if __name__ == "__main__":
    main()