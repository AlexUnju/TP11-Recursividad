# x = 345

def sd(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sd(int(n / 10))

x = int(input('x:'))
print(sd(x))

#------------------------------------------------------

# n10 = 2835 , foranea = 16

def acad(n, b):
    tcon = "0123456789ABCDEF"
    if n < b:
        return tcon[n]
    else:
        return acad(n // b, b) + tcon[n % b]

n10 = int(input('Nro:'))
foranea = int(input('Foránea:'))
print(acad(n10, foranea))

#---------------------------------------------------------

# n = 7091 nro = 584

def modRec(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + modRec(int(s[:-1]))

n = int(input('nro:'))
print(modRec(n))

#----------------------------------------------------------

# nro = 584

def misterio(n):
    if n < 10:
        return (10 * n) + n
    else:
        a = misterio(n // 10)
        b = misterio(n % 10)
        return (100 * a) + b


