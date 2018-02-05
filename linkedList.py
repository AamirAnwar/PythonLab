'''Linked list data structure using lists'''
from time import sleep

# Linked list node structure
class Node:
    def __init__(self, data, ptr):
        self.ptr = ptr
        self.data = data


class LinkedList:
    def __init__(self):
        self.root = None


    def isEmpty(self):
        return True if self.root == None else False

    def __str__(self):
        if self.isEmpty():
            return "Empty Linked List -> NULL"
        else:
            string = ""
            p = self.root
            while p.ptr:
                p = p.ptr
                string += "{} -> ".format(p.data)
            string += "NULL"
            return string



    def addNode(self, data):
        newNode = Node(data, None)
        if self.isEmpty():
            # Linked list is empty
            self.root =  newNode
            return self.root
        else:
            p = self.root
            while p.ptr:
                p = p.ptr

            p.ptr = newNode
            return self.root



    def deleteNode(self, data):
        p = self.root
        while p.ptr and p.ptr.data != data:
            p = p.ptr

        if p.ptr:
            sleep(1)
            print("Deleting {} from linked list...".format(data))
            temp = p.ptr
            p.ptr = p.ptr.ptr
            temp = None
            sleep(1)
            print("Aaand it's gone!")
        else:
            print("{} is not in the linked list!".format(data))
