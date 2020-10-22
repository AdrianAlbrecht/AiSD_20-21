def number(n: int):
    if n==0:
        return f'0'
    return f'{n}, {number(n-1)}'

def fib(n: int):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

def power(number: int, n: int):
    if n==0:
        return 1
    return number*power(number,n-1)

def reverse(txt: str):
    if len(txt)==1:
        return f'{txt}'
    return f'{txt[-1]}{reverse(txt[:len(txt)-1])}'

def factorial(n: int):
    if n==1:
        return 1
    return n*factorial(n-1)

def prime(n: int):
    if n==1:
        return False
    if n==2:
        return True
    i=1
    while (i*i<n):
        if(prime(i)):
            if (n%i==0):
                return False
        i+=1
    return True


def n_sums(n: int):
    #TO DO
    return []

def combinations(n: int):
    #TO DO
    return [[],[]]

def remove_duplicates(txt: str):
    if len(txt)==1:
        return f'{txt}'
    if txt[0]==txt[1]:
        return f'{remove_duplicates(txt[1:])}'
    return f'{txt[0]}{remove_duplicates(txt[1:])}'


def balanced_parentheses(n:int):
    if(n%2==1):
        return None
    if (n==2):
        return ["()"]
    results=[]
    for x in balanced_parentheses(n-2):
        results.append("()"+x)
        results.append("("+x+")")
        if(x!="()"*(int)((n/2)-1)):
            results.append(x+"()")
    return results


print(number(5))
print(fib(12))
print(power(2,9))
print(reverse("Banda"))
print(factorial(5))
print(prime(97))
print(prime(98))
print(n_sums(3))
print(combinations(3))
print(remove_duplicates("XXYZZZ"))
print(balanced_parentheses(8))

