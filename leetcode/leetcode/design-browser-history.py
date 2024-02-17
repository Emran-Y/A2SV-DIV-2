class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode
        self.curr = newNode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.val