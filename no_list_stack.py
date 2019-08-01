class EmptyStack(Exception):
    pass

class StackItem():
    def __init__(self, value):
        self.value = value
        self.previous_item = None

class NoListStack():
    def __init__(self):
        self.size = 0
        self.stack_head = None
    
    def push(self, value):
        i = StackItem(value)
        previous_item = self.stack_head
        self.stack_head = i
        if self.size > 0:
            self.stack_head.previous_item = previous_item
        self.size = self.size + 1
    
    def pop(self):
        try:
            if self.size > 0:
                item_to_pop = self.stack_head.value
                if self.size == 1:
                    self.stack_head.previous_item = None
                else:
                    self.stack_head = self.stack_head.previous_item
                self.size = self.size - 1                
                return item_to_pop
            else:
                raise EmptyStack
        except:
            print("The Stack is already empty.")

if __name__ == "__main__":
    stack = NoListStack()
    stack.push("A")
    print(stack.stack_head.value)
    stack.push("B")    
    print(stack.stack_head.value)    
    stack.push("C")
    print(stack.stack_head.value)    
    stack.push("D")    
    print(stack.stack_head.value)
    print("----")
    print(stack.size)    
    print("----")
    a = stack.pop()
    print(a)    
    a = stack.pop()
    print(a)    
    a = stack.pop()
    print(a)    
    a = stack.pop()
    print(a)
    a = stack.pop()
