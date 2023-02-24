def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def factor_2(n):
    factor = 1
    for i in range(1,n+1):
        factor = factor*i
    return factor

if __name__ == '__main__':
    print(factor_2(56))