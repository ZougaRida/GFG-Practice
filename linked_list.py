class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Node(data={self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_node(self, data):
        if self.length == 0:
            self.head = Node(data)
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.length += 1

    def pop_node(self):
        if self.length == 0:
            raise IndexError("Linked List is already empty")

        elif self.length == 1:
            popped_data = self.head.data
            self.head = None
            self.tail = None
            self.length = 0
            return popped_data

        else:
            popped_data = self.tail.data
            node = self.head
            while node.next is not self.tail:
                node = node.next

            self.tail = node
            self.tail.next = None
            self.length -= 1
            return popped_data

    def __len__(self):
        return self.length

    def __str__(self):
        node = self.head
        result = ""
        while node is not None:
            result += f"{node} -> "
            node = node.next
        result += "None"
        return result

    def __repr__(self):
        return self.__str__()
