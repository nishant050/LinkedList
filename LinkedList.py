class Node():
  def __init__(self, value, next_node = None):
    self.value = value
    self.next_node = next_node
  def get_next_node(self):
    return self.next_node
  def set_next_node(self, next_node):
    self.next_node = next_node
  def get_value(self):
    return self.value
    
class LinkedList():
  def __init__(self, value = None):
    self.head_node = Node(value)
  def get_head_node(self):
    return self.head_node
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    if self.head_node.get_value() != None:
      new_node.set_next_node(self.head_node)
    self.head_node = new_node
  def stringify_list(self):
    current_node = self.get_head_node()
    string_list = ''
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + '\n'
        current_node = current_node.get_next_node()
    return string_list
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()

    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

def generate_test_list(length):
  test_list = LinkedList()
  for i in range(length,0,-1):
    test_list.insert_beginning(i)
  return test_list

sample = generate_test_list(7)



