from ds.singly import Node

class TestNode:
    def test_init(self):
        item = 1
        node = Node(item)
        assert type(node) is Node
        assert type(node.data) is type(item)
        assert node.data == item
        assert node.next is None

    def test_chain(self):
        item = "word"
        node = Node(item)
        assert str(node) == item
        assert type(node) is Node
        assert type(node.data) is type(item)
        assert node.data == item
        assert node.next is None




