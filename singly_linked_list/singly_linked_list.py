class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty linked list
        if self.head is None and self.tail is None:
            return
        # list with 1 node
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = None

        self.tail = current
        return value

    def contains(self, value):
        if self.head is None:
            return False
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        # iterate through all elements
        cur_node = self.head.get_next()
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        return cur_max
