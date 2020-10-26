class Node:
    def __init__(self, val, next_field=None, previous_field=None):
        self.value = val
        self.next = next_field
        self.prev = previous_field


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.prev = new_node
            self.head = new_node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value, None, curr)

    def set_head(self, index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        self.head = curr
        curr.prev = None
        return True

    def access(self, index):
        if self.head is None:
            return False

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        return curr.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        new_node = Node(value, curr, curr.prev)
        curr.prev.next = new_node
        # curr.prev = new_node
        return True

    def remove(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return True
            else:
                return False

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        if curr is None:
            return False
        prev = curr.prev

        prev.next = curr.next
        curr.next.prev = prev
        return True

    def __str__(self) -> str:
        if self.head is None:
            return '[]'
        curr = self.head
        result = '['
        while curr.next is not None:
            result += f'{curr.value}, '
            curr = curr.next
        result += f'{curr.value}]'
        return result

    def print(self):
        """정방향 프린트"""
        if self.head is None:
            print('[]')
        else:
            curr = self.head
            result = '['
            while curr.next is not None:
                result += f'{curr.value}, '
                curr = curr.next
            result += f'{curr.value}]'
            print(result)

    def reverse_print(self):
        """역방향 프린트"""
        if self.head is None:
            print('[]')
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        result = '['
        while curr.prev is not None:
            result += f'{curr.value}, '
            curr = curr.prev
        result += f'{curr.value}]'
        print(result)

    def test(self):
        curr = my_list.head
        if curr is not None:
            next_list = []
            prev_list = []
            while curr.next is not None:
                next_list.append(curr)
                curr = curr.next

            while curr.prev is not None:
                prev_list.append(curr)
                curr = curr.prev
            print(next_list)
            print(prev_list)


my_list = DoublyLinkedList()
# my_list.print()

for i in range(10):
    my_list.append(i + 1)

# my_list.print()

for i in range(10):
    my_list.prepend(i + 1)

# my_list.print()

value = my_list.access(3)
# print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
# my_list.print()

my_list.remove(4)
# my_list.print()

# my_list.set_head(10)
my_list.print()
my_list.reverse_print()
