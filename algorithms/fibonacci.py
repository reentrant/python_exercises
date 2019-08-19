def iter_fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        temp = current + after
        print(i, temp, current, after)
        current = after
        after = temp
    return current


def dynamic_fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    # breakpoint()
    return fib[n]


if __name__ == '__main__':
    print(iter_fibonacci(2))
    print(dynamic_fibonacci(2))
