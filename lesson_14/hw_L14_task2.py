class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, elements):
        self.stack.append(elements)

    def pop(self):
        deleted_item = self.stack.pop()
        return deleted_item

    def is_empty(self):
        return self.stack == []

    def peek(self):
        if self.stack == []:
            return None
        else:
            return self.stack[-1]


class IncorrectUserInput(Exception):
    ...


def closed_brackets(brackets: str) -> bool:
    my_stack = Stack()
    balanced = my_stack.is_empty()
    for symbol in brackets:
        if symbol not in '([{}])':
            raise IncorrectUserInput("Object must consist only of brackets.")
        if symbol == '(' or symbol == '[' or symbol == '{':
            my_stack.push(symbol)
        else:
            if my_stack.is_empty():
                balanced = False
            elif (symbol == ')' and my_stack.peek() == '(') or \
                    (symbol == ']' and my_stack.peek() == '[') or \
                    (symbol == '}' and my_stack.peek() == '{'):
                my_stack.pop()
            else:
                balanced = False
    balanced = my_stack.is_empty()
    return balanced


print(closed_brackets('(())[][]{{{{{{{}}}}}}}'))
print(closed_brackets('{{{}}}({}[{})'))
print(closed_brackets('[{(((){}{[]]}))}]'))
print(closed_brackets('(())[][]{{{{{{{}}}}}}}s'))
