def is_empty(stack):
    return len(stack) == 0

def is_left_bracket(char):
    return char in BRACKET_MAP.values()

BRACKET_MAP = {
    "}": "{", #: "}",
    "]": "[", #: "]",
    ")": "(", #: ")",
}

def valid_parentheses(input):
    stack = []
    for char in input:
        if(is_left_bracket(char)):
            stack.append(char)
        else:
            if is_empty(stack): return False
            top_char_in_stack = stack.pop()

            if top_char_in_stack != BRACKET_MAP[char]: return False
    
    return is_empty(stack)


def main():
    input = "{[()]}["
    result = valid_parentheses(input)
    print(result)

if __name__ == "__main__":
    main()
