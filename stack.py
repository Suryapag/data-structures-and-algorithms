class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack elements

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items.pop()  # Remove and return the top item of the stack
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items[-1]  # Return the top item of the stack without removing it
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)  # Return the number of elements in the stack


# Example usage:
stack = Stack()  # Create a new instance of the Stack class

stack.push(1)  # Push elements onto the stack
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())  # Print the size of the stack
print("Top element:", stack.peek())  # Print the top element of the stack

print("Popping elements:")
while not stack.is_empty():  # Pop and print all elements until the stack is empty
    print(stack.pop())
