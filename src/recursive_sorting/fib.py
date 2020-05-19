# A Fibonacci number is compriosed of the value of two previous fib numbers in sequence
# to find out the nth fib number, need to know values of predecessors
# f(n) = f(n-1) + f(n-2)


def fib(n):
    # base case
    # test for negs (TODO)
    # if n is 0
    if n == 0:
        return 0
    # if n is 1
    if n == 1:
        return 1
    # if not base case
    # use recursion fib(n-1)
    return fib(n-1) + fib(n-2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
