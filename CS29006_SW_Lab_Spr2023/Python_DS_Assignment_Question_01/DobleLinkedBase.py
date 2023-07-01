class _DoubleLinkedBase:
    """ A base class providing a doubly linked list representation."""

    class _Node:
        """ Lightweight, nonpublic class for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next' # streamline memory

        def __init__(self, element, prev, next): # initialize node's fields
            self._element = element   
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0 # number of elements

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return true if list is empty"""
        if(self._size == 0):
                return True
        else:
                return False

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its elements"""

        temp = node._prev
        temp._next = node._next
        temp = node._next
        temp._prev = node._prev
        self._size -= 1
        return node._element

a = _DoubleLinkedBase()
a._insert_between(10, a._header, a._trailer)
a._insert_between(20, a._header._next, a._trailer)
print(a.__len__())
print(a._delete_node(a._header._next))
print(a._delete_node(a._header._next))
print(a.__len__())
print(a.is_empty())
