string = input()

n = len(string)


def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term.
    """
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[-1]

def factorial(n):
    """
    Calculate the factorial of a number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# print(fibonacci(4))
l, r = 0, 0
cnt = 0
res = 0
while r < n:
    if string[r] == 'm' or string[r] == 'w':
        print(0)
        exit()
    elif string[r] == 'u' :
        while r < n and string[r] == 'u':
            r += 1
        # print(fibonacci(r - l))
        if fibonacci(r - l + 1) > 1:
            res += fibonacci(r - l + 1)
        cnt = 1
        # print(fibonacci(r - l + 1), 'here')
    elif string[r] == 'n':
        while r < n and string[r] == 'n':
            r += 1
        # print(l, r)
        if fibonacci(r - l + 1) > 1:
            res += fibonacci(r - l + 1)
        cnt = 1
        # print(fibonacci(r - l + 1), 'here')
    elif l < r:
        while l < r:
            l += 1
    else:
        l += 1
        r += 1

if res == 0:
    res += cnt
print(res)

            

        