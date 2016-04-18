"""
It is important to note that we could have chosen to implement the stack
using a list where the top is at the beginning instead of at the end. In
this case, instead of using `pop` and `append` as above, instead we
would pop from and insert into position 0. Here is a possible
implementation of that approach:
"""

class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

"""
This ability to change the physical implementation of an abstract data
type while maintaining the logical characteristics is an example of
abstraction at work. However, even though the stack will work either
way, if we consider the performance of the two implementations, there is
definitely a difference. Recall that the `append` and `pop()` operations
were both $$O(1)$$. This means that the first implementation will
perform push and pop in constant time no matter how many items are on
the stack. The performance of the second implementation suffers in that
the `insert(0)` and `pop(0)` operations will both require $$O(n)$$ for a
stack of size n. Clearly, even though the implementations are logically
equivalent, they would have very different timings when performing
benchmark testing.

Going forward, we will simply use Python `list`s directly as stacks,
being careful to only use the stack-like behavior of the `list`.
"""
