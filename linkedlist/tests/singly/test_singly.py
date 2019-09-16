from ds.singly import LinkedList, Node

import pytest



class TestSingly:
    def test_init(self):
        sll = LinkedList()
        assert len(sll) == 0
        assert sll.size == 0
        assert sll.head is None

    def test_push(self):
        sll = LinkedList()
        begin = -40
        end = 10
        for i in range(begin, end):
            sll.push(i)
        assert len(sll) == abs(end-begin)
        assert sll.size == abs(end-begin)
        assert sll.head != None
        assert sll.head.data == end-1
        assert sll.head.next.data == end-2

    def test_push_alphabet(self):
        sll = LinkedList()
        assert sll.size == 0
        assert sll.head is None
        alphabet = list(map(chr, range(97, 123)))
        for letter in alphabet:
            sll.push(letter)
        assert sll.size == 26
        assert sll.head is not None

    def test_pop(self):
        sll = LinkedList()
        end = 10
        assert sll.size == 0
        assert sll.head is None
        for i in range(end):
            sll.push(i)
            assert sll.head is not None
            assert sll.size == 1
            assert sll.pop() is not None
            assert sll.size == 0
            assert sll.head is None
        for j in range(end):
            sll.push(j)
        assert sll.size == end
        assert sll.head is not None
        for k in range(end):
            assert sll.pop() is not None
        assert sll.size == 0
        assert sll.head is None

    def test_pop_empty(self):
        sll = LinkedList()
        with pytest.raises(IndexError):
            sll.pop()

    def test_iter(self):
        sll = LinkedList()
        items = 10
        assert sll.head is None
        assert sll.size == 0
        for i in range(items):
            assert sll.push(i) is None
        for node in sll:
            assert node.data == items-1
            items -= 1
        assert type(sll.head) is Node

    def test_append(self):
        sll = LinkedList()
        items = 10
        assert sll.head is None
        assert sll.size == 0
        for i in range(items):
            assert sll.append(i) is None
            assert sll.size == i+1
        assert type(sll.head) is Node
        assert sll.size == items
        counter = 0
        for node in sll:
            assert node.data == counter
            counter += 1

    def test_insert(self):
        sll = LinkedList()
        items = 10
        assert sll.head is None
        assert sll.size == 0
        for i in range(items-1,-1,-1):
            assert sll.insert(i) is None
        assert type(sll.head) is Node
        assert sll.size == items
        counter = 0
        for node in sll:
            assert node.data == counter
            counter += 1

    def test_remove(self):
        sll = LinkedList()
        items = 10
        assert sll.head is None
        assert sll.size == 0
        for i in range(items):
            assert sll.push(i) is None
        assert type(sll.head) is Node
        assert sll.size == items
        assert sll.remove(items) is False
        assert type(sll.head) is Node
        assert sll.size == items
        for j in range(items-1,-1,-1):
            assert sll.remove(j) is True
        assert sll.head is None
        assert sll.size == 0

    def test_remove_at(self):
        sll = LinkedList()
        items = 10
        assert sll.head is None
        assert sll.size == 0
        for i in range(items):
            assert sll.push(i) is None
        assert type(sll.head) is Node
        assert sll.size == items
        for i in range(items-1,-1,-1):
            assert sll.remove_at(i) is None
        assert sll.head is None
        assert sll.size == 0

    def remove_at_empty(self):
        sll = LinkedList()
        with pytest.raises(IndexError):
            sll.remove_at(0)

    def remove_at_out_of_range(self):
        sll = LinkedList()
        assert sll.head is None
        assert sll.size == 0
        assert sll.push(1) is None
        assert type(sll.head) is Node
        assert sll.size == 1
        with pytest.raises(IndexError):
            sll.remove_at(-1)




