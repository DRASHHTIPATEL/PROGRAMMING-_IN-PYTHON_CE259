# Implement a stack like structure.

class Stack:

# Initializing stack.

def __init__(self):

self.stack = []

# Function push to push the element

def push(self, value):

self.stack.append(value)

# Function pop to delete the top most element

def pop(self):

if self.is_Empty():

print("Stack is Empty!!\n")

else:

self.stack.pop()

# Function to check if the stack is empty or not.

def is_Empty(self):

return self.stack == []

# Function to traverse the stack.

def traversal(self):

print(f' stack = {self.stack[::-1]}')

# Creating an object of stack.

s = Stack()

# Giving choice to the user.

print("Enter from below option : \n")

while True:

print("1. push")

print("2. pop")

print("3. traversal")

print("4. isEmpty")

print("5. Quit.")

choice = int(input())

if choice == 1:

print("Enter element : ")

element = int(input())

s.push(element)

elif choice == 2:

s.pop()

elif choice == 3:

s.traversal()

elif choice == 4:

status = s.is_Empty()

print(f'Empty Status : {status}\n')

elif choice == 5:

break

else:

print("Enter proper choice!!\n")

continue
