from ds.doubly import LinkedList, Node, sublist

import pytest

class TestDoubly:
    def test_init(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.size == 0

    def test_push(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == 1
        assert dll.head.data == dll.tail.data
        assert dll.push(2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.head.next == dll.tail
        assert dll.tail.prev == dll.head
        assert dll.size == 2
        assert dll.head.data != dll.tail.data
        assert dll.head.data == 2
        assert dll.tail.data == 1

    def test_push_multiple(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items):
            assert dll.push(i) is None
            assert isinstance(dll.head, Node)
            assert dll.size == i+1
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        assert dll.head.data != dll.tail.data
        assert dll.head.data == items-1
        assert dll.tail.data == 0

    def test_pop_single_default(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert dll.head.next is None
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert dll.tail.next is None
        assert dll.tail.prev is None
        assert dll.head.data == dll.tail.data
        assert dll.size == 1
        single = dll.pop()
        assert isinstance(single, Node)
        assert single.data == 1
        assert single.next is None
        assert single.prev is None
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_pop_single_negative(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert dll.head.next is None
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert dll.tail.next is None
        assert dll.tail.prev is None
        assert dll.head.data == dll.tail.data
        assert dll.size == 1
        single = dll.pop(-1)
        assert isinstance(single, Node)
        assert single.data == 1
        assert single.next is None
        assert single.prev is None
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_pop_heads(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(items-1, -1, -1):
            assert isinstance(dll.head, Node)
            head = dll.pop()
            assert isinstance(head, Node)
            assert head.data == j
            assert dll.size == items - (items-j)
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        
    def test_pop_heads_negative(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(items-1, -1, -1):
            assert isinstance(dll.head, Node)
            head = dll.pop(-(j+1))
            assert isinstance(head, Node)
            assert head.data == j
            assert dll.size == items - (items-j)
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_pop_tails(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items-1,-1,-1):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(items-1,-1,-1):
            assert isinstance(dll.tail, Node)
            tail = dll.pop(j)
            assert isinstance(tail, Node)
            assert tail.data == j
            assert tail.next == None
            assert dll.size == items - (items-j)
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_pop_tails_negative(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items-1,-1,-1):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(items-1,-1,-1):
            assert isinstance(dll.tail, Node)
            tail = dll.pop(-1)
            assert isinstance(tail, Node)
            assert tail.data == j
            assert tail.next == None
            assert dll.size == items - (items-j)
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_pop_2nd(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items-1,-1,-1):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(1,items-1):
            second = dll.pop(1)
            assert isinstance(second, Node)
            assert second.next is None
            assert second.prev is None
            assert second.data == j
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.head.data == 0
        assert dll.tail.data == items-1
        assert dll.size == 2

    def test_pop_2nd_negative(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items-1,-1,-1):
            assert dll.push(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.size == items
        for j in range(items-2, 0, -1):
            second = dll.pop(-2)
            assert isinstance(second, Node)
            assert second.next is None
            assert second.prev is None
            assert second.data == j
        assert isinstance(dll.head, Node)
        assert isinstance(dll.head.next, Node)
        assert dll.head.prev is None
        assert isinstance(dll.tail, Node)
        assert isinstance(dll.tail.prev, Node)
        assert dll.tail.next is None
        assert dll.head.data == 0
        assert dll.tail.data == items-1
        assert dll.size == 2

    def test_pop_empty(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        with pytest.raises(IndexError):
            dll.pop()

    def test_pop_out_of_range_positive(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == 1
        with pytest.raises(IndexError):
            dll.pop(2)

    def test_pop_out_of_range_negative(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == 1
        with pytest.raises(IndexError):
            dll.pop(-2)

    def test_iter(self):
        dll = LinkedList()
        items = 10
        counter = 0
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items):
            assert dll.append(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == items
        for node in dll:
            assert isinstance(node, Node)
            assert isinstance(node.data, int)
            counter += 1
        assert counter == items

    def test_append_empty(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.append(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head.data == dll.tail.data
        assert dll.head is dll.tail
        assert dll.size == 1

    def test_append_multiple(self):
        dll = LinkedList()
        items = 100
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        for i in range(items):
            assert dll.append(i) is None
            assert dll.size == i+1
            assert dll.tail.data == i
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.size == items
        for j in range(items):
            assert dll.pop().data == j
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_remove_head(self):
        dll = LinkedList()
        items = 2
        assert dll.is_empty()
        for i in range(items):
            assert dll.append(i) is None
        assert dll.size == items
        assert dll.head is not dll.tail
        assert dll.remove(0) is None
        assert dll.head is dll.tail
        assert dll.size == items-1

    def test_remove_tail(self):
        dll = LinkedList()
        items = 2
        assert dll.is_empty()
        for i in range(items):
            assert dll.append(i) is None
        assert dll.size == items
        assert dll.tail is not dll.head
        assert dll.remove(1) is None
        assert dll.head is dll.tail
        assert dll.size == items-1

    def test_remove_mid(self):
        dll = LinkedList()
        items = 3
        assert dll.is_empty()
        for i in range(items):
            assert dll.append(i) is None
        assert dll.size == items
        assert dll.head is not dll.tail
        assert dll.remove(1) is None
        assert dll.head is not dll.tail
        assert dll.head.data == 0
        assert dll.tail.data == 2
        assert dll.head.next is dll.tail
        assert dll.tail.prev is dll.head
        assert dll.head.prev is None
        assert dll.tail.next is None
        assert dll.size == items-1

    def test_remove_single(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(1) is None
        assert dll.size == 1
        assert dll.head is dll.tail
        assert dll.remove(1) is None
        assert dll.is_empty()

    def test_remove_empty(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.size == 0
        with pytest.raises(ValueError):
            dll.remove(0)

    def test_remove_not_found(self):
        dll = LinkedList()
        assert dll.is_empty() is True
        assert dll.push(1) is None
        assert dll.is_empty() is False
        with pytest.raises(ValueError):
            dll.remove(2)

    def test_reverse(self):
        dll = LinkedList()
        items = 100
        assert dll.is_empty()
        assert dll.reverse() is None
        assert dll.is_empty()
        for i in range(items):
            assert dll.append(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == items
        assert dll.head is not dll.tail
        assert dll.head.data == 0
        assert dll.head.prev is None
        assert dll.tail.data == items-1
        assert dll.tail.next is None
        assert dll.reverse() is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == items
        assert dll.head is not dll.tail
        assert dll.head.data == items-1
        assert dll.head.prev is None
        assert dll.tail.data == 0
        assert dll.tail.next is None
        match = items-1
        for node in dll:
            assert node.data == match
            match -= 1
        assert dll.reverse() is None
        match = 0
        for node in dll:
            assert node.data == match
            match += 1

    def test_extend_another_linked_list(self):
        first = LinkedList()
        second = LinkedList()
        items = 100
        for i in range(items):
            assert first.append(i) is None
        for j in range(items,items*2):
            assert second.append(j) is None
        assert first.extend(second) is None
        assert isinstance(first.head, Node)
        assert isinstance(first.tail, Node)
        assert first.head is not second.head
        assert first.tail is not second.tail
        assert first.size == items*2
        match = 0
        for node in first:
            assert node.data == match
            match += 1

    def test_extend_another_linked_list_from_empty(self):
        first = LinkedList()
        second = LinkedList()
        items = 100
        for i in range(items):
            assert second.append(i) is None
        assert first.is_empty()
        assert second.size == items
        assert first.extend(second) is None
        assert isinstance(first.head, Node)
        assert isinstance(first.tail, Node)
        assert first.head is not second.head
        assert first.tail is not second.tail
        assert first.size == second.size
        match = 0
        for node in first:
            assert node.data == match
            match += 1

    def test_extend_iterable_object(self):
        items = 100
        first = LinkedList()
        second = list(range(items))
        assert first.is_empty()
        assert first.extend(second) is None
        assert isinstance(first.head, Node)
        assert isinstance(first.tail, Node)
        assert first.head is not first.tail
        assert first.size == len(second)
        match = 0
        for node in first:
            assert node.data == match
            match += 1

    def test_extend_non_iterable_object_error(self):
        dll = LinkedList()
        with pytest.raises(TypeError):
            dll.extend(None)


    def test_clear(self):
        dll = LinkedList()
        items = 100
        assert dll.is_empty()
        for i in range(items):
            assert dll.append(i) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.size == items
        assert dll.clear() is None
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0

    def test_clear_empty(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.clear() is None
        assert dll.is_empty()

    def test_insert_empty(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.insert(0,0) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1

    def test_insert_new_head(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(1) is None
        assert isinstance(dll.head, Node) 
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1
        assert dll.insert(0,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 2
        assert dll.tail.data == 1
        assert dll.head.next is dll.tail
        assert dll.head.prev is None
        assert dll.tail.prev is dll.head
        assert dll.tail.next is None
        assert dll.size == 2

    def test_insert_new_head_negative(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1
        assert dll.insert(-1,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 2
        assert dll.tail.data == 1
        assert dll.head.next is dll.tail
        assert dll.head.prev is None
        assert dll.tail.prev is dll.head
        assert dll.tail.next is None
        assert dll.size == 2

    def test_insert_new_head_negative_out_of_bounds(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1
        assert dll.insert(-1000,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 2
        assert dll.tail.data == 1
        assert dll.head.next is dll.tail
        assert dll.head.prev is None
        assert dll.tail.prev is dll.head
        assert dll.tail.next is None
        assert dll.size == 2

    def test_insert_new_tail(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1
        assert dll.insert(1,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 1
        assert dll.tail.data == 2
        assert dll.head.next is dll.tail
        assert dll.head.prev is None
        assert dll.tail.prev is dll.head
        assert dll.tail.next is None
        assert dll.size == 2

    def test_insert_new_tail_out_of_bounds(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.push(0) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is dll.tail
        assert dll.size == 1
        assert dll.insert(1000,1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 0
        assert dll.tail.data == 1
        assert dll.head.next is dll.tail
        assert dll.head.next.data == 1
        assert dll.head.prev is None
        assert dll.tail.prev is dll.head
        assert dll.tail.prev.data == 0
        assert dll.tail.next is None
        assert dll.size == 2

    def test_insert_end(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.append(0) is None
        assert dll.append(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.size == 2
        assert dll.insert(1,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 0
        assert dll.tail.data == 1
        assert dll.head.next is not dll.tail
        assert dll.head.next.data == 2
        assert dll.head.next.prev is dll.head
        assert dll.head.prev is None
        assert dll.tail.prev is not dll.head
        assert dll.tail.prev.data == 2
        assert dll.tail.prev.next is dll.tail
        assert dll.tail.next is None
        assert dll.size == 3

    def test_insert_end_negative(self):
        dll = LinkedList()
        assert dll.is_empty()
        assert dll.append(0) is None
        assert dll.append(1) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.size == 2
        assert dll.insert(-1,2) is None
        assert isinstance(dll.head, Node)
        assert isinstance(dll.tail, Node)
        assert dll.head is not dll.tail
        assert dll.head.data == 0
        assert dll.tail.data == 1
        assert dll.head.next is not dll.tail
        assert dll.head.next.data == 2
        assert dll.head.prev is None
        assert dll.tail.prev is not dll.head
        assert dll.tail.prev.data == 2
        assert dll.tail.next is None
        assert dll.size == 3

    def test_is_empty(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.is_empty() is True

    def test_is_empty_2(self):
        dll = LinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size == 0
        assert dll.append(1) is None
        assert dll.is_empty() is False

    def test_sublist_negative_start(self):
        with pytest.raises(IndexError):
            LinkedList().sublist(-1,0)

    def test_sublist_negative_end(self):
        with pytest.raises(IndexError):
            LinkedList().sublist(0,-1)

    def test_sublist_start_out_of_bounds(self):
        with pytest.raises(IndexError):
            LinkedList().sublist(1,0)

    def test_sublist_end_out_of_bounds(self):
        with pytest.raises(IndexError):
            LinkedList().sublist(0,1)

    def test_sublist_equal_start_and_end(self):
        with pytest.raises(IndexError):
            LinkedList().sublist(0,0)

    def test_sublist_start_greater_than_end(self):
        items = 10
        dll = LinkedList()
        for i in range(items):
            dll.push(i)
        with pytest.raises(IndexError):
            dll.sublist(3,2)
    
    def test_util_sublist_invalid_type(self):
        with pytest.raises(TypeError):
            sublist(None)

    def test_util_sublist_negative_start(self):
        with pytest.raises(IndexError):
            sublist(LinkedList(),-1,0)

    def test_util_sublist_negative_end(self):
        with pytest.raises(IndexError):
            sublist(LinkedList(),0,-1)

    def test_util_sublist_start_out_of_bounds(self):
        with pytest.raises(IndexError):
            sublist(LinkedList(),1,0)

    def test_util_sublist_end_out_of_bounds(self):
        with pytest.raises(IndexError):
            sublist(LinkedList(),0,1)

    def test_util_sublist_equal_start_and_end(self):
        with pytest.raises(IndexError):
            sublist(LinkedList(),0,0)

    def test_util_sublist_start_greater_than_end(self):
        with pytest.raises(IndexError):
            items = 10
            dll = LinkedList()
            for i in range(items):
                dll.push(i)
            sublist(dll,3,2)

    def test_sublist(self):
        dll = LinkedList()
        items = 10
        start,end = 0,3
        assert dll.head is None
        assert dll.size == 0
        for i in range(items):
            assert dll.push(i) is None
        assert type(dll.head) is Node
        assert dll.size == 10
        sl = sublist(dll,start,end)
        assert type(sl) is LinkedList
        assert type(sl.head) is Node
        assert sl.size == (end-start)
        compare = items-1
        for node in sl:
            assert node.data == compare
            compare -=1

    def test_sublist_halves(self):
        dll = LinkedList()
        items = 10
        assert dll.head is None
        assert dll.size == 0
        for i in range(items):
            assert dll.push(i) is None
        dll.reverse()
        
        def halves(linked_list, begin, end):
            mid = linked_list.size // 2
            left = sublist(linked_list, begin, mid)
            right = sublist(linked_list, mid, end)
            return left, right
        
        def print_list(linked_list):
            for node in linked_list:
                print(node.data, end=',')
            print(" ")

        def check(linked_list):
            if linked_list.size <= 2:
                return
            left, right = halves(linked_list, 0, linked_list.size)
            if linked_list.size % 2:  # Odds
                assert left.size == (linked_list.size//2)
                assert right.size == (linked_list.size//2+1)
            else:  # Evens
                assert left.size == (linked_list.size//2)
                assert right.size == (linked_list.size//2)
            print_list(left)
            print_list(right)
            check(left)
            check(right)

        check(dll)




