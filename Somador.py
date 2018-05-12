def somador(a, b, cin, vet, c=1, d=2):
    c += 1
    d -= 1
    xor1 = a[d] ^ b[d]
    and1 = a[d] and b[d]
    xor2 = cin ^ xor1
    and2 = cin and xor1
    cout = and1 or and2
    vet[c] = xor2
    if c == 3:
        vet[c + 1] = cout
        vet = vet[::-1]
        print('Soma em binario: ', end="")
        for i in range(len(vet)):
            print(vet[i], end="")
        print('\nSoma em decimal: ', binadec(vet))
    if c == 2:
        somador(a, b, cout, vet, c, d)


def psomador(a, b, vet):
    xor1 = a[3] ^ b[3]
    and1 = a[3] and b[3]
    xor2 = a[2] ^ b[2]
    xor3 = and1 ^ xor2
    and2 = xor2 and and1
    and3 = a[2] and b[2]
    vai = and3 or and2
    vet[0] = xor1
    vet[1] = xor3
    somador(a, b, vai, vet)


def binadec(x):
    soma = 0
    x = x[::-1]
    for c in range(len(x)):
        soma += x[c] * (2 ** c)
    return soma


print('*='*20)
print(' '*8, '\033[4;34mCALCULADORA BINARIA\033[m')
print('*='*20)
vet = [0, 0, 0, 0, 0]
a = []
b = []
e = 1
while e != 0:
    x = input('Digite um binario de 4 bits: ')
    a = [int(d) for d in x]
    for c in range(4):
        if a[c] not in (1, 0):
            e = 1
        else:
            e = 0
e = 1
f = binadec(a)
while e != 0:
    y = input('Digite outro binario de 4 bits: ')
    b = [int(d) for d in y]
    for c in range(4):
        if b[c] not in (1, 0):
            e = 1
        else:
            e = 0
g = binadec(b)
print('A em decimal: ', f)
print('B em decimal: ', g)
psomador(a, b, vet)
