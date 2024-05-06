# Create a node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the linked list
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Create a linked list Obj
linked_list = LinkedList()

# Add some nodes to the linked list
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

# Print the linked list
linked_list.print_list()