import LinkedList

def get_middle(sample_list):
  fast = sample_list.head_node
  slow = sample_list.head_node
  while fast:
    fast = fast.get_next_node()
    if fast:
      fast = fast.get_next_node()
      slow = slow.get_next_node()
  return slow

test1 = generate_test_list(7)
print(test1.stringify_list())
middle = get_middle(test1)
print(middle.get_value())
