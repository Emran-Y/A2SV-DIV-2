from math import inf

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class RecentCounter:
    def __init__(self):
        self.count = 0
        self.dummyNode_head = Node(-inf)
        self.dummyNode_tail = Node(inf)
        self.dummyNode_tail.prev = self.dummyNode_head
        self.dummyNode_head.next = self.dummyNode_tail

    def ping(self, t: int) -> int:
        self.count += 1

        # Adding the new request to the tail
        prev_node = self.dummyNode_tail.prev
        new_node = Node(t)
        new_node.prev = prev_node
        new_node.next = self.dummyNode_tail
        self.dummyNode_tail.prev = new_node
        prev_node.next = new_node

        # Removing outdated requests from the head
        while self.dummyNode_head.next.val < (t - 3000):
            self.count -= 1
            temp = self.dummyNode_head.next.next
            self.dummyNode_head.next = temp
            temp.prev = self.dummyNode_head

        return self.count