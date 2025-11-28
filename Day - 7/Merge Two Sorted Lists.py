class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        c = d
        while a and b:
            if a.val <= b.val:
                c.next = ListNode(a.val); a = a.next
            else:
                c.next = ListNode(b.val); b = b.next
            c = c.next
        while a:
            c.next = ListNode(a.val); a = a.next; c = c.next
        while b:
            c.next = ListNode(b.val); b = b.next; c = c.next
        return d.next