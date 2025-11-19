def fib(n):
    global fib_dict
    if fib_dict.get(n) != None:
        return fib_dict[n]

    if n % 2 == 0:
        fib_dict[n] = ((fib(n//2) + 2 * fib((n//2) - 1)) * fib(n//2)) % 1000000007
        return fib_dict.get(n)
    else:
        fib_dict[n] = (fib((n+1)//2) ** 2 + fib((n+1)//2 - 1) ** 2) % 1000000007
        return fib_dict.get(n)
    
if __name__ == "__main__":
    fib_dict = {}
    fib_dict[0] = 0
    fib_dict[1] = 1

    n = int(input())

    print(fib(n) % 1000000007)