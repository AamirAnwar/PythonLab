print("Welcome to Python Lab!")

from linkedList import LinkedList
import random

ll = LinkedList()
data = [random.randint(1,1000) for x in range(10)]

for i in data:
    ll.addNode(i)

for i in range(len(data)):
    randIndex = random.randint(0,len(data) - 1)
    ll.deleteNode(data[randIndex])

print(ll)





