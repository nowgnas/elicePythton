class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self, head):
        self.head = head
        self.tail = head

    def addToEnd(self, node):
        self.tail.next = node
        self.tail = node

    def deleteElement(self):
        pass
