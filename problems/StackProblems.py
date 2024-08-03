from DS.ListStack import ListStack as Stack

def sort_stack(random_stack: Stack):
    sorted_stack = Stack()
    while not random_stack.is_empty():
        current_num = random_stack.pop()
        
        if sorted_stack.is_empty() or sorted_stack.peek() <= current_num:
            sorted_stack.push(current_num)
        else:
            while sorted_stack.peek() > current_num:
                random_stack.push(sorted_stack.pop())
            sorted_stack.push(current_num)
    return sorted_stack

def main():
    random_stack = Stack()
    random_stack.push(5)
    random_stack.push(1)
    random_stack.push(3)
    random_stack.push(2)
    sorted_stack = sort_stack(random_stack)
    print(sorted_stack)


if __name__ == '__main__':
    main()