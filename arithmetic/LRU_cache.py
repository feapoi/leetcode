class LinkList:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = LinkList()
        self.tail = LinkList()
        self.capacity = capacity
        self.size = 0

        self.head.next = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        thisNode = self.cache[key]
        self.del_node(thisNode)
        self.add_node_to_top(thisNode)
        return thisNode.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            newNode = LinkList()
            newNode.key = key
            newNode.val = value
            self.cache[key] = newNode
            if self.capacity > self.size:
                self.add_node_to_top(newNode)
                self.size += 1
            else:
                delNode = self.tail.prev
                self.del_node(delNode)
                del self.cache[delNode.key]
                self.add_node_to_top(newNode)
        else:
            oldNode = self.cache[key]
            self.del_node(oldNode)
            oldNode.val = value
            self.add_node_to_top(oldNode)

    def del_node(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    # 两个节点间的四根线
    def add_node_to_top(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


cache = LRUCache(2)
cache.put(2, 1)
print(cache.get(2))
cache.put(2, 2)

