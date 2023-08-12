class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def Iter(p=0):
            nonlocal l1,l2
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + p
            p = s//10
            
            l1, l2 = l1.next if l1 else 0, l2.next if l2 else 0

            return ListNode(s%10, Iter(p) if l1 or l2 or p else None)

        return Iter()