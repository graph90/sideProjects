class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    def insertAfter(self, prevNode, data):
        if prevNode is None:
            print('Previous node is not in the list')
            return
        node = Node(data)
        node.next = prevNode.next
        prevNode.next = node
        node.prev = prevNode
        if node.next is not None:
            node.next.prev = node
    def insertBefore(self, nextNode, data):
        if nextNode is None:
            print('Next node is not in the list')
            return
        node = Node(data)
        node.prev = nextNode.prev
        nextNode.prev = node
        node.next = nextNode
        if node.prev is not None:
            node.prev.next = node
    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp is None:
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
    def deleteNodeAtPosition(self, pos):
        if self.head is None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
def main():
    doublyLinkedList = DoublyLinkedList()
    doublyLinkedList.append(1)
    doublyLinkedList.append(2)
    doublyLinkedList.append(3)
    doublyLinkedList.append(4)
    doublyLinkedList.append(5)
    doublyLinkedList.printList()
    doublyLinkedList.prepend(0)
    doublyLinkedList.printList()
    doublyLinkedList.insertBefore(doublyLinkedList.head.next, 1.5)
    doublyLinkedList.printList()
    doublyLinkedList.insertAfter(doublyLinkedList.head.next, 1.75)
    doublyLinkedList.printList()
    doublyLinkedList.deleteNode(1.75)
    doublyLinkedList.printList()
    doublyLinkedList.deleteNodeAtPosition(2)
    doublyLinkedList.printList()
if __name__ == '__main__':
    main()