from ds.doubly import Node


class TestNode:
    def test__init__(self):
        value = 1
        node = Node(value)
        assert type(node) is Node
        assert type(node.data) is type(value)
        assert node.data == value
        assert node.next is None
        assert node.prev is None
   
    def test__str__(self):
        value = "word"
        node = Node(value)
        assert str(node) == value
        assert type(node) is Node
        assert type(node.data) is type(value)
        assert node.data == value
        assert node.next is None
        assert node.prev is None

    def test__eq__(self):
        node1 = Node(1)
        assert (node1 == Node(1)) is True
        assert (node1 == Node(2)) is False
        assert (node1 == Node([])) is False
        assert (node1 == Node(True)) is False
        assert (node1 == []) is False
        assert (node1 == 1) is False

    def test__ne__(self):
        assert (Node(1) != Node(3)) is True
        assert (Node(1) != Node(1)) is False
        assert (Node(1) != Node(True)) is True
        assert (Node(1) != Node({})) is True
        assert (Node(1) != []) is True
        assert (Node(1) != 1) is True

    def test__lt__(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        assert (node2 < node1) is False
        assert (node2 < node3) is True
        assert (node2 < 2) is False

    def test__le__(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(2)
        assert (node2 <= node1) is False
        assert (node2 <= node3) is True
        assert (node2 <= node4) is True
        assert (node2 <= 2) is False

    def test__gt__(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        assert (node2 > node1) is True
        assert (node2 > node3) is False
        assert (node2 > 2) is False

    def test__ge__(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(2)
        assert (node2 >= node1) is True
        assert (node2 >= node3) is False
        assert (node2 >= node4) is True
        assert (node2 >= 2) is False






