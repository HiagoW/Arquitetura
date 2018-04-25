from array import array
def func(x, y):
    vet=[]
    c=0
    while x>0:
        i=x%y
        if y==16:
            if i==10:
                i='A'
            if i==11:
                i='B'
            if i==12:
                i='C'
            if i==13:
                i='D'
            if i==14:
                i='E'
            if i==15:
                i='F'
        vet.append(i)
        x=x//y
        c+=1
    vet.reverse()
    for i in range(c):
        print(vet[i], end="")

x=int(input('Digite o numero que deseja converter: '))
y=0
while y not in (2,8,16):
    y=int(input('Digite a base para conversao[2,8 ou 16]'))
func(x,y)
