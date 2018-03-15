l = [[1, 2, 3, 4], [5, 6, 7, 8]]
m = len(l)
n = len(l[0])


def isWithinBounds(a, b):
    if a > m - 1 or b > n - 1:
        return False
    else:
        return True


def move(a, b, p):
    global l
    if isWithinBounds(a, b):

        # If we've reached the bottom right cell print path up till now
        if l[a][b] == l[len(l) - 1][len(l[0]) - 1]:
            print("Reached bottom right! P => {}".format(p + [l[a][b]]))
            print(p + [l[a][b]])
            return True

    if isWithinBounds(a, b + 1):
        # Go right
        print("Going right with P => {}".format(p + [l[a][b]]))
        move(a, b + 1, p + [l[a][b]])

    if isWithinBounds(a + 1, b):
        # Go down
        print("Going down with P => {}".format(p + [l[a][b]]))
        move(a + 1, b, p + [l[a][b]])


move(0, 0, [])