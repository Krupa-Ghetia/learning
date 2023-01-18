class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]



if __name__ == "__main__":
    my_stack = Stack()
    
    print(my_stack.is_empty())
    print(len(my_stack))
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(5)
    print(my_stack.is_empty())
    print(len(my_stack))
    print(my_stack.peek())
    print(my_stack.pop())
    print(len(my_stack))
