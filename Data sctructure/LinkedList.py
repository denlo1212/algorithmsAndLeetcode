class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:

    def __init__(self):
        # dummy node
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0

        while current:
            if i == index:
                return current.value
            i += 1

            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node

    def insertTail(self, val: int) -> None:

    def remove(self, index: int) -> bool:

    def getValues(self) -> List[int]:
