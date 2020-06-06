from node import Node

class Stack:
  def __init__(self):
    self.top_item = None
  
  # Define your push() and pop() methods below:
  def push(self, value):
    self.item = Node(value, self.top_item)
    #self.item.set_next_node(self.top_item)
    self.top_item = self.item
    
  def pop(self):
    self.item_to_remove = self.top_item
    self.top_item = self.top_item.get_next_node()
    return self.item_to_remove.value

  def peek(self):
    return self.top_item.get_value()