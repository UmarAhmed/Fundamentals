
# Simple implementation of singly linked lists
# Includes some common functions and implementations of algorithms

# Indexing: O(n) (getting an item is linear)
# Insert/Delete: O(1) (when done at the head node)
# Searching/Insertion/Deleting: O(n)


class Node:
    def __init__(self, initdata, n=None):
        self.data = initdata
        self.next = n

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def search(self, item):  # returns index of item
        index = 0
        current = self.head
        while current:
            if current.data == item:
                return index
            else:
                index += 1
                current = current.next
        return False

    def remove(self, item):  # requires item is in the linked list
        current = self.head
        prev = None
        while current:
            if current.data == item:
                if prev is None:
                    self.head = current.next
                    break
                else:
                    prev.next = current.next
                    break
            else:
                prev = current
                current = current.next

    def reverse(self):
        prev = None
        while self.head:
            current = self.head
            self.head, current.next, prev = self.head.next, prev, current
        self.head = prev

    def reverse_between(self, m, n):
        if m == n:
            return self.head

        dummy = LinkedList()
        dummy.next = self.head
        prev = dummy

        for _ in range(m - 1):
            prev = prev.next

        rev = None
        current = prev.next
        for _ in range(n - m + 1):
            temp = current.next
            current.next = rev
            rev = current
            current = temp

        prev.next.next = current
        prev.next = rev

        return dummy.next

    def append(self, item):
        current = self.head
        if current:
            while current.next:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_print(self):
        h = self.head
        while h:
            h = h.next
            print(h.data)


# Inserts Node(data) at position and returns a linked list
def insert_nth(head, data, position):
    if position == 0:
        return Node(data, head)
    else:
        current = head
        i = 1
        while position - i > 0:
            current = current.next
            i += 1
        if current.next is None:
            current.next = Node(data)
            return head
        else:
            prev = current.next
            current.next = Node(data, prev)
            return head


# deletes node at index, returns linked list
def delete(head, index):
    if index == 0:
        return head.next
    else:
        head.next = delete(head.next, index - 1)
        return head


# Uses hash set to find the merge point, O(n) space and O(n) time
#   Returns False if there is no merge point
# See below for a better way to go about this
def find_merge_node1(a, b):
    nodes = set()
    while a:
        nodes.add(a.data)
        a = a.next
    while b:
        if b.data in nodes:
            return b.data
        else:
            b = b.next
    return False


# This basically connects the two linked lists and uses the fact
# that the linked list after merge point has the same length
# but requires that they indeed merge
def find_merge_node(head_a, head_b):
    a = 0
    b = 0
    while True:
        if a >= 2 or b >= 2:
            return False
        if head_a.data == head_b.data:
            return head_a.data
        if head_a.next is None:
            head_a = head_b
            a += 1
        if head_a.next is None:
            head_b = head_a
            b += 1
        else:
            head_a, head_b = head_a.next, head_b.next


# Floyd's cycle finding algorithm
def has_cycle(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # can change to return the cycle node
    return False
