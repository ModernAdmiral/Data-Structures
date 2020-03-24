from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # should add an item to the back of the queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1
    # should remove and return an item from the front of the queue.

    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        return self.storage.remove_from_head()

    # return the number of items in the queue

    def len(self):
        return self.size
