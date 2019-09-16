class Node:
    """Used to represent Nodes within a Doubly-LinkedList."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Next Node
        self.prev = None  # Prev Node

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data is other.data
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.data is not other.data
        else:
            return True

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.data >= other.data
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.data > other.data
        else:
            return False

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.data <= other.data
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.data < other.data
        else:
            return False



class LinkedList:
    """Doubly LinkedList Implementation."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        """Returns the number of nodes in the LinkedList."""
        return self.size

    def __iter__(self) -> None:
        """Initializes iterator to the head of the LinkedList."""
        self.iter = self.head
        return self

    def __next__(self) -> Node:
        """Sets iterator to the next node and returns the current node."""
        if self.iter is None:
            raise StopIteration
        else:
            node = self.iter
            self.iter = self.iter.next
            return node

    def is_empty(self) -> None:
        """Checks if LinkedList is empty."""
        return self.head is None and self.tail is None and self.size == 0

    def push(self, data) -> None:
        """Adds new node to the front of the LinkedList.

        Args:
            data: Any type of data to be put into LinkedList.
        """
        if self.is_empty():  # Add first Node
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            self.head.prev = Node(data)  # Make previous Node the new head Node
            self.head.prev.next = self.head  # Set previous Node to point to the old head Node
            self.head = self.head.prev
            self.size += 1

    def pop(self, index=0) -> Node:
        """Removes and returns node at index (default first).

        Args:
            index: Specified index (starts at zero).

        Returns:
            Node at index (default first).

        Raises:
            IndexError: If LinkedList is empty.
        """
        if self.is_empty():  # Empty
            raise IndexError('pop from empty LinkedList')
        if index < 0:  # Try to change negative index to positive index
            index = self.size + index
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        elif index == 0 and self.size == 1:  # Remove one and only item
            node = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return node
        elif index == 0:  # Remove head
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            node.next = None
            self.size -= 1
            return node
        elif index == self.size-1:  # Remove tail
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
            self.size -= 1
            return node
        else:
            node = None
            head_distance = 0 + index
            tail_distance = (self.size-1) - index
            if head_distance <= tail_distance:
                node = self.head  # Iterate from head
                for i in range(index):
                    node = node.next
            else:
                node = self.tail  # Iterate from tail
                for j in range((self.size-1)-index):
                    node = node.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            self.size -= 1
            return node

    def append(self, data) -> None:
        """Appends node to the end of the LinkedList.

        Args:
            data: Object being put into the LinkedList.
        """
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            node = Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
            self.size += 1

    def insert(self, index: int, data) -> None:
        """Inserts a new node with specified data at index into the LinkedList.

        Args:
            index: Specified index.
            data: Object being put inside a new node.
        """
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return None
        if index < 0:  # Try to change to a positive index
            index = self.size + index
        if index <= 0:  # Make new head
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.size += 1
        elif index >= self.size:  # Make new tail
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.size += 1
        elif index > 0:
            current = None
            head_distance = 0 + index
            tail_distance = (self.size-1) - index
            if head_distance <= tail_distance:
                current = self.head  # Iterate from head
                for i in range(index):
                    current = node.next
            else:
                current = self.tail  # Iterate from tail
                for j in range((self.size-1)-index):
                    current = node.prev
            new_node = Node(data)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def remove(self, data) -> None:
        """Removes the specified data from the LinkedList.

        Args:
            data: The data being removed from the LinkedList.

        Raises:
            IndexError: If LinkedList is empty.
        """
        if self.is_empty():
            raise ValueError('remove from empty LinkedList')
        elif self.size == 1:
            if self.head.data == data:
                self.head = None
                self.tail = None
                self.size = 0
                return None
        else:
            current = self.head
            while current is not None:
                if current.data == data:
                    if current is self.head:
                        target = self.head
                        self.head = self.head.next
                        self.head.prev = None
                        target.next = None
                    elif current is self.tail:
                        target = self.tail
                        self.tail = self.tail.prev
                        self.tail.next = None
                        target.prev = None
                    else:
                        target = current
                        current = current.next
                        current.prev = target.prev
                        target.prev.next = current
                        target.next = None
                        target.prev = None
                    self.size -= 1
                    return None
                else:
                    current = current.next
        raise ValueError('remove(x): x not in LinkedList')

    def reverse(self) -> None:
        """Reverses the order of the LinkedList."""
        if self.size > 1:
            self.tail = self.head
            current = self.head
            next_node = current.next
            while next_node is not None:  # Stops at the last node
                current.next = current.prev
                current.prev = next_node
                current = next_node
                next_node = next_node.next
            current.next = current.prev  # Change last node manually
            current.prev = None
            self.head = current

    def extend(self, iterable) -> None:
        """Deep copy of an iterable object into LinkedList.

        Args:
            iterable: Iterable object

        Raises:
            TypeError: 'iterable' object is not iterable
        """
        if isinstance(iterable, LinkedList):
            for node in iterable:
                if self.head is None:
                    self.head = Node(node.data)
                    self.tail = self.head
                    self.size += 1
                else:
                    self.tail.next = Node(node.data)
                    self.tail.next.prev = self.tail
                    self.tail = self.tail.next
                    self.size += 1
        else:
            try:
                for item in iterable:
                    if self.head is None:
                        self.head = Node(item)
                        self.tail = self.head
                        self.size += 1
                    else:
                        self.tail.next = Node(item)
                        self.tail.next.prev = self.tail
                        self.tail = self.tail.next
                        self.size += 1
            except TypeError:
                print('\'{}\' object is not iterable'.format(type(iterable)))
                raise

    def clear(self) -> None:
        """Removes all items from LinkedList"""
        if isinstance(self.head, Node):
            current = self.head
            while current is not None:
                next_node = current.next
                current.data = None
                current.prev = None
                current.next = None
                current = None
                current = next_node
            current = None
            self.head = None
            self.tail = None
            self.size = 0

    def sort(self) -> None:
        def split(linked_list: LinkedList) -> Node:
            pass
        if self.size > 1:
            mid = self.size // 2




    def sublist(self, start=0, end=0) -> 'LinkedList':
        """Returns LinkedList based on specified indexes.

        Args:
            start: Specified starting index, included in LinkedList.
            end: Specified ending index, not included in LinkedList.

        Returns:
            LinkedList with only the specified nodes.

        Raises:
            IndexError: If arguments are either out of range, equal to each other, or invalid.
        """
        if start < 0 or start > self.size:
            raise IndexError('\'start\' argument out of range')
        elif end < 0 or end > self.size:
            raise IndexError('\'end\' argument out of range')
        elif start == end:
            raise IndexError('\'start\' and \'end\' arguments are equal')
        elif start > end:
            raise IndexError('\'start\' argument greater than \'end\' argument')
        else:
            current = linked_list.head
            for i in range(start):  # Set pointer to specified 'start' index
                current = current.next
            rv = LinkedList()
            rv.append(current.data)
            for j in range((end-start)-1):
                current = current.next
                rv.append(current.data)
            return rv






def sublist(linked_list: LinkedList, start=0, end=0) -> LinkedList:
    """Returns sublist based on specified indexes.

    Args:
        linked_list: Object of type `LinkedList`.
        start: Specified starting index, included in LinkedList.
        end: Specified ending index, not included in LinkedList.

    Returns:
        LinkedList with only the specified nodes.

    Raises:
        TypeError: If function applied to an object of different type.
        IndexError: If arguments are either out of range, equal to each other, or invalid.
    """
    if type(linked_list) is not LinkedList:
        raise TypeError('object not of type: LinkedList')
    elif start < 0 or start > linked_list.size:
        raise IndexError('\'start\' argument out of range')
    elif end < 0 or end > linked_list.size:
        raise IndexError('\'end\' argument out of range')
    elif start == end:
        raise IndexError('\'start\' and \'end\' arguments are equal')
    elif start > end:
        raise IndexError('\'start\' argument greater than \'end\' argument')
    else:
        current = linked_list.head
        for i in range(start):  # Set pointer to specified 'start' index
            current = current.next
        rv = LinkedList()
        rv.push(current.data)
        for j in range((end-start)-1):
            current = current.next
            rv.append(current.data)
        return rv


def mergesort(linked_list: LinkedList):
    def merge(linked_list: LinkedList, left, right):
        pass

    def mergesort(linked_list: LinkedList, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mergesort(linked_list, left, mid)
        mergesort(linked_list, mid+1, right)
