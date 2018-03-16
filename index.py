
print("Welcome to Python Lab!")
'''
The Python Playground!
'''

# For n disks, total 2^n – 1 moves are required.
def towersOfHanoi(n,from_stack,to_stack,aux_stack):
    if n == 1:
        print("Moved disc {} from {} to {}".format(n,from_stack, to_stack))
    else:
        towersOfHanoi(n-1, from_stack, aux_stack, to_stack)
        print("Moved disc {} from {} to {}".format(n,from_stack, to_stack))
        towersOfHanoi(n - 1, aux_stack, to_stack, from_stack)




def test():
    n = 4
    towersOfHanoi(n,'A', 'B', 'C')

test()