class ListStack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
    
    def __str__(self):
        last_index = len(self.stack_list) - 1

        item_str = "["
        for index, item in enumerate(self.stack_list):
            item_str += f"{item}"
            if index != last_index:
                item_str += ", "
        item_str += "]"
        return item_str