def cut(n):
    factors=[]
    for x in range(1, n+1):
        if n % x == 0:
            factors.append(x)
    return factors

def dup(n, t):
    multiples=[]
    i=1
    while i < t+1:
        multiples.append(n*i)
        i+=1
    return multiples

def eql(n1, n2):
    cf=[]
    n1f = cut(n1)
    n2f = cut(n2)
    for x in n1f:
        for y in n2f:
            if x==y:
                cf.append(x)
    return cf

