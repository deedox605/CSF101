from collections import deque
class queue:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise Infexerror("queue is empty")
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise Indexerror("queue is empty")
    def size(self):
        return len(self.items)
queue=queue()
queue.enqueue("TAsk 1")
queue.enqueue("TAsk 2")
queue.enqueue("task 3")

print(queue.dequeue())
print(queue.front())
print(queue.size())