""" Implementing Collatz conjecture in Python """

def f(n):
    if (n%2==0):
        n = n // 2
        return n
    else:
        n = 3 * n + 1
        return n
    
n = f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
print(n)
