class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head:ListNode):
    """
    :type head: ListNode
    :rtype: bool
    """
    nodes_seen = set()
    current = head
    while current is not None:
        if current in nodes_seen:
            return True
        nodes_seen.add(current)
        current = current.next
    return False


head = [3,2,0,-4]
pos = 1
print(hasCycle(head))