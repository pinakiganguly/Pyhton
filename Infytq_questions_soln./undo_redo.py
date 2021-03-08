class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      counter+=1
      temp = temp.next

    return counter
def text_editor(text, pattern):

  u = Stack()
  r = Stack()

  for i in text:
    u.push(i)

  for i in pattern:

    if i == 'u':
      data = u.pop()
      r.push(data)
    else:
      data = r.pop()
      u.push(data)

  res = ""

  while(not u.is_empty()):
    res = u.pop() + res

  print(res)


  
text_editor("Haldia","u,r,r")