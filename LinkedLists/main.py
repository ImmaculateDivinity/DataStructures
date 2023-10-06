# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
head = { "value": 3,
       "next": {
              "value": 2,
              "next": {
                     "value": 1,
                     "next": None
              }
       }
       }
print(head["next"]["next"]["value"])
"""
class Node:
       def __init__(self, value):
              self.value = value
              self.next = None
class LinkedList:
       def __init__(self, value):
              new_node = Node(value)
              self.head = new_node
              self.tail = new_node
              self.length = 1
       def print_list (self):
              temp = self.head
              while temp is not None:
                     print(temp.value)
                     temp = temp.next
       def append(self, value):
              new_node = Node(value)
              if self.length == 0:
                     self.head = new_node
                     self.tail = new_node
              else:
                     self.tail.next = new_node
                     #changes the pointer
                     self.tail = new_node
              self.length += 1
              return True
              #return is not necessary
       def pop(self):
              if self.length == 0:
                     return None
              temp = self.head
              pre = self.head
              while(temp.next):
                     pre = temp
                     temp = temp.next
              self.tail = pre
              self.tail.next = None
              self.length -= 1
              if self.length == 0:
                     self.head = None
                     self.tail = None
              return temp.value
                     #returns item popped
       def prepend(self, value):
              new_node = Node(value)
              if self.length == 0:
                     self.head = new_node
                     self.tail = new_node
              else:
                     new_node.next = self.head
                     self.head = new_node
              self.length += 1
              return True
       def FirstPop(self):
              if self.length == 0:
                     return None
              temp = self.head
              self.head = self.head.next
              temp.next = None
              self.length -= 1
              if self.length == 0:
                     self.head = None
                     self.tail = None
              return temp
       def get(self, index):
              if index < 0 or index >= self.length:
                     return None
              temp = self.head
              for _ in range(index):
                     temp = temp.next
              return temp
       def set_value(self, index, value):
              temp = self.get(index)
              #method in another method, returns node or none
              if temp is not None:
                     temp.value = value
                     return True
              return False
       def insert(self, index, value):
              if index < 0 or index > self.length:
                     return False
              if index == 0:
                     return self.preprend(value)
              if index == self.length:
                     return self.append(value)
              new_node = Node(value)
              temp = self.get(index - 1)
              new_node.next = temp.next
              temp.next = new_node
              self.length += 1
              return True
       def remove(self, index):
              if index < 0 or index >= self.length:
                     return None
              if index == 0:
                     return self.FirstPop()
              if index == (self.length - 1):
                      return self.pop()
              prev = self.get(index - 1)
              temp = prev.next
              prev.next = temp.next
              temp.next = None
              self.length -= 1
              return temp
       #reverse function is a common interview question (corporate)
       def reverse(self):
              temp = self.head
              self.head = self.tail
              self.tail = temp
              after = temp.next
              before = None
              for _ in range(self.length):
                     after = temp.next
                     temp.next = before
                     before = temp
                     temp = after
                     #complicated conceptualization
my_linked_list = LinkedList(2)
my_linked_list.append(1)
my_linked_list.append(12)
my_linked_list.reverse()

my_linked_list.print_list()


