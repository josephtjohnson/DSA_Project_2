from time import time

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

def union(llist_1, llist_2):
    # Your Solution Here
    union_list = []

    if llist_1.head is not None:

        node = llist_1.head

        while node:
            union_list.append(node.value)
            node = node.next

    if llist_2.head is not None:

        node = llist_2.head

        while node:
            union_list.append(node.value)
            node = node.next
      
    return build_linkedlist(sorted(set(union_list)))


def intersection(llist_1, llist_2):
    # Your Solution Here
    
    if llist_1.head and llist_2.head:

        llist_1_list = []
        intersection_list = []

        node = llist_1.head

        while node:
            llist_1_list.append(node.value)
            node = node.next

        node = llist_2.head

        while node:
            if node.value in llist_1_list:
                intersection_list.append(node.value)
            node = node.next

        if len(intersection_list) == 0:
            return None

        else:
            return build_linkedlist(sorted(set(intersection_list)))
    else:
        return None


def build_linkedlist(set1):

    llist = LinkedList()

    for i in set1:
        llist.append(i)
    return llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

t0 = time()

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

t1 = time() - t0

print("Run time analysis: {} seconds".format(round(t1, 5)))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

t0 = time()

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

t1 = time() - t0

print("Run time analysis: {} seconds".format(round(t1, 5)))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

t0 = time()

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

t1 = time() - t0

print("Run time analysis: {} seconds".format(round(t1, 5)))

# Test Case 4
linked_list_7 = None
linked_list_8 = LinkedList()

element_2 = [1,7,8,9,11,21,1]

t0 = time()

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

t1 = time() - t0

print("Run time analysis: {} seconds".format(round(t1, 5)))

# Test Case 5
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [-100, 100]
element_2 = [1,7,8,9,11,21,1]

t0 = time()

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

t1 = time() - t0

print("Run time analysis: {} seconds".format(round(t1, 5)))
