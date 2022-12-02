from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    linkedlist1 = a.head
    linkedlist2 = b.head

    if linkedlist1 is None and linkedlist2:
        return LinkedList(linkedlist2)
    if linkedlist2 is None and linkedlist1:
        return LinkedList(linkedlist1)

    while linkedlist1 and linkedlist2:
        temp1 = linkedlist1.next
        temp2 = linkedlist2.next
        linkedlist1.next = linkedlist2
        if temp1:
            linkedlist2.next = temp1
        linkedlist1 = temp1
        linkedlist2 = temp2
    return a
