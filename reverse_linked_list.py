from linked_list import Node, LinkedList

def reverse_linked_list(head: Node) -> Node:
    """
    This function reverses a linked list using slow and fast pointers technique.
    Time complexity: O(n), Memory complexity: O(1).
    https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1
    """

    # BY THE WAY, this is DEFINITELY not the advised way to reverse the linked list
    # the better way was to implement a method withing the LinkedList class to reverse it
    # or better yet take advantage of reverse iterator to do so which will do later
    # TODO: implement reverse iterator in the nearest future
    # The TODO is DONE and implemented.
    slow = None
    fast = head
    while fast is not None:
        temporary = fast.next
        fast.next = slow
        slow = fast
        fast = temporary
    return slow



if __name__ == "__main__":
    linked_list = LinkedList()
    [linked_list.push_node(int(x)) for x in input().split()]
    print(linked_list)
    head = reverse_linked_list(linked_list.head)
    while head is not None:
        print(head.data, end="-> ")
        head = head.next
    print("None")
