class Node:
    def __init__(self, value=0, next = None):
        self.value = value
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def get(self, index: int) -> int:
        if index >=  self.length:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.value
    def addAtHead(self, val: int) -> None:
        head = Node(val)
        head.next = self.head
        self.head = head
        self.length += 1
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        dummy = Node(next = self.head)
        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.head = dummy.next
        self.length += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.length:
            newNode = Node(value = val)
            dummy = Node(next = self.head)
            curr = dummy
            for i in range(index):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
            self.head = dummy.next
            self.length += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            dummy = Node(next = self.head)
            curr = dummy
            for i in range(index):
                curr = curr.next
            curr.next = curr.next.next
            self.length -= 1
            self.head = dummy.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)