def p_three(n):
    i = 0
    while i < n:
        yield 3 ** i
        i += 1

for x in p_three(5):
    print(x)
