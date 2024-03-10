# Define a class node which will be the blueprint for each of the nodes
class Node:
    def __init__(self, data):
        self.data = data  # Data that was passed during instantiation will be stored here
        self.next = None  # This will act as a pointer to the next node in the list. When creating a new node it always points to Null/None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
        print()


if __name__ == '__main__':
    first_linked_list = LinkedList()
    first_linked_list.print_list()
    # Prints out an empty list

    first_linked_list.append(11)
    first_linked_list.append(22)
    first_linked_list.append(33)
    first_linked_list.append(44)
    first_linked_list.print_list()
    # 11 22 33 44
