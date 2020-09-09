class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def _add_all_to_ll(head, llist, seen_before):
    node = head
    while node:
        if node.value not in seen_before:
            llist.append(node.value)
            seen_before.add(node.value)
        node = node.next

def _add_only_seen_to_ll(head, llist, seen_before):
    node = head
    while node:
        if node.value in seen_before:
            llist.append(node.value)
            seen_before.remove(node.value)
        node = node.next

# Union runtime: O(n)
# The reason this is N is because I only run through each list once and
# append to the end of the list once.  We know working with sets runs in
# O(1) and we know that we drop the constants from the runtime final calculation
def union(llist_1, llist_2):
    seen_before = set()
    LLfinal = LinkedList()
    if llist_1 is not None:
        _add_all_to_ll(llist_1.head, LLfinal, seen_before)
    if llist_2 is not None:
        _add_all_to_ll(llist_2.head, LLfinal, seen_before)
    return LLfinal
    
# Intersection runtime: O(n)
# The reason this is N is because I only run through each list once and
# append to the end of the list once.  We know working with sets runs in
# O(1) and we know that we drop the constants from the runtime final calculation
def intersection(llist_1, llist_2):
    if llist_1 is None or llist_2 is None:
        return LinkedList()
    seen_before = set()
    node = llist_1.head
    LLFinal = LinkedList()
    while node:
        seen_before.add(node.value)
        node = node.next

    _add_only_seen_to_ll(llist_2.head, LLFinal, seen_before)
    return LLFinal


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# See comments above union for runtime and comments above intersection for runtime.

print("\nTest Case 3 - None type linked list")
llist1 = None
llist2 = [1,2,4,5,6,7,8,9]
sample_list = LinkedList()
for i in llist2:
    sample_list.append(i)
print(intersection(llist1, sample_list))
# Doesn't print anything - empty linked list returned

print("\nTest Case 4 - None type linked list")
llist1 = None
llist2 = [1,2,4,5,6,7,8,9]
sample_list = LinkedList()
for i in llist2:
    sample_list.append(i)
print(union(llist1, sample_list))
# 1 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 ->

