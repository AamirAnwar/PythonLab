# A host of problems solved using dynamic programming
import time
def testDynamicFibo(numberToFind):

    size = numberToFind + 1
    store = [-1] * (size)
    store[0] = 0
    store[1] = 1

    def fibo(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibo(n - 1) + fibo(n - 2)

    def dp_fibo(n):
        for i in range(2, n + 1):
            store[i] = store[i - 1] + store[i - 2]
        return store[n]

    start = time.time()
    print(fibo(numberToFind))
    print("Exponential solution--- %s seconds ---" % round(time.time() - start, 3))

    start = time.time()
    print(dp_fibo(numberToFind))
    print("Dynamic Programming Solution--- %s seconds ---" % round(time.time() - start, 3))
