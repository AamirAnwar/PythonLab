'''Implementations of the stack data structure in python'''

'''1) Array Implementation'''

class Stack:
    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)
        print("Pushed {}".format(data))

    def pop(self):
        if not self.isEmpty():
            popped = self.list.pop()
            print("Popping stack now! Element remove is {}".format(popped))
            return popped
        else:
            print("Empty Stack!")

    def isEmpty(self):
        if len(self.list) <= 0:
            return True

    def peek(self):
        if len(self.list) > 0:
            return self.list[len(self.list) - 1]
