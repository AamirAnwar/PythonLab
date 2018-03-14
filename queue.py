'''Queue data structure'''

'''Using lists'''
class Queue:
    def __init__(self):
        self.list = []


    def isEmpty(self):
        return True if len(self.list) <= 0 else False

    def enqueue(self, data):
        self.list.append(data)
        # print("Added {} to the queue".format(data))

    def dequeue(self):
        if not self.isEmpty():
            item = self.list.pop(0)
            # print("Dequeued item {}".format(item))
            return item
        else:
            print("Queue is empty!!")

    def front(self):
        if not self.isEmpty():
            # print("{} is at the front of the queue".format(self.list[0]))
            return self.list[0]
        else:
            print("Queue is empty!!")

    def end(self):
        if not self.isEmpty():
            last = self.list[len(self.list) - 1]
            # print("{} is at the end of the queue".format(last))
            return last
        else:
            print("Queue is empty!!")


