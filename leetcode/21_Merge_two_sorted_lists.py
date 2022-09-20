# ou are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val < l2.val:
        tmp = head = ListNode(l1.val)
        l1 = l1.next
    else:
        tmp = head = ListNode(l2.val)
        l2 = l2.next
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            tmp.next = ListNode(l1.val)
            l1 = l1.next
        else:
            tmp.next = ListNode(l2.val)
            l2 = l2.next
        tmp = tmp.next
    while l1 is not None:
        tmp.next = ListNode(l1.val)
        l1 = l1.next
        tmp = tmp.next
    while l2 is not None:
        tmp.next = ListNode(l2.val)
        l2 = l2.next
        tmp = tmp.next
    return head

def printList(node: ListNode):
    while node is not None:
        print(str(node.val), end=" ")
        node = node.next
    print()

if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)
    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)
    printList(merge_two_lists(head1, head2))
