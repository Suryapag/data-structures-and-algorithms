class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to store queue elements

    def is_empty(self):
        return len(self.items) == 0  # Check if the queue is empty

    def enqueue(self, item):
        self.items.append(item)  # Add an item to the rear of the queue

    def dequeue(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items.pop(0)  # Remove and return the front item of the queue
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():  # Check if the queue is not empty
            return self.items[0]  # Return the front item of the queue without removing it
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)  # Return the number of elements in the queue


# Example usage:
queue = Queue()  # Create a new instance of the Queue class

queue.enqueue(1)  # Enqueue elements to the queue
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Print the size of the queue
print("Front element:", queue.peek())  # Print the front element of the queue

print("Dequeuing elements:")
while not queue.is_empty():  # Dequeue and print all elements until the queue is empty
    print(queue.dequeue())
