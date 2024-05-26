from DS.LinkedList import LinkedList


def find_kth_from_end(ll: LinkedList, k):
    slow = fast = ll.head
    for iter in range(k):
        if fast == None:
            return None
        fast = fast.next
    
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow