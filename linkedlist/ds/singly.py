class Node:
    """Used to represent Nodes within a Singly-LinkedList."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)



class LinkedList:
    """Singly LinkedList Implementation."""
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> None:
        self.iter = self.head
        return self

    def __next__(self) -> Node:
        if self.iter is None:
            raise StopIteration
        else:
            node = self.iter
            self.iter = self.iter.next
            return node

    def push(self, data) -> None:
        """Pushes new node to the front of the LinkedList.

        Args:
            data: Any type of data to be put into LinkedList.
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self) -> Node:
        """Removes node from the head of the LinkedList.

        Returns:
            Node from the head of the LinkedList.

        Raises:
            IndexError: If LinkedList is empty.
        """
        if self.head is None:
            raise IndexError('pop from empty LinkedList')
        else:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node

    def append(self, data) -> None:
        """Appends a node to the end of the LinkedList.

        Args:
            data: Any type of data being put into the LinkedList.
        """
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
            self.size += 1

    def insert(self, data) -> None:
        """Inserts a node within the LinkedList in sorted order.

        Args:
            data: Generic type of data
        """
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        elif self.head.data >= data:  # Special case for head, duplicates allowed.
            node = Node(data)
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            current = self.head
            while current.next is not None and current.next.data < data:  # Compare next's data.
                current = current.next
            node = Node(data)
            node.next = current.next
            current.next = node
            self.size += 1

    def remove(self, data) -> bool:
        """Removes a node containing a certain key.

        Args:
            data: The data we are looking for.

        Returns:
            True: If the Node is removed successfully.
            False: If the data is not found.

        Raises:
            IndexError: If LinkedList is empty.
        """
        if self.head is None:
            raise IndexError('remove from empty LinkedList')
        elif self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    self.size -= 1
                    return True
                else:
                    current = current.next
            return False

    def remove_at(self, index: int) -> None:
        """Removes a node at a specified index.

        Args:
            index: Array-like index within the LinkedList.

        Returns:
            True: Node is removed successfully from the LinkedList.
            False: Specified index is not valid.
        """
        if self.head is None:
            raise IndexError('removing from empty LinkedList')
        elif index < 0 or index >= self.size:
            raise IndexError('removal index out of range')
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
            self.size -= 1
