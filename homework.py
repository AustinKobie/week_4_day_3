class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
        
def sorted_input_list(func):
    def list_sort(l):
        return func(sorted(l))
    return list_sort


@sorted_input_list
def convert_to_linked_list(l):
    head = Node(l[0])
    current_node = head
    for value in l[1:]:
        current_node.next = Node(value)
        current_node = current_node.next
    return head


list = [55,23,79,10,356,9,6,0]
head = convert_to_linked_list(list)

current_node = head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
