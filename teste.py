from array import array
def dectobase(x, y):
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

def basetodec(x, y):
	soma=0
	if y==16:
		vet=[d for d in x]
		for c in range(len(vet)):
			if vet[c].upper()=='A':
				vet[c]='10'
			if vet[c].upper()=='B':
				vet[c]='11'
			if vet[c].upper()=='C':
				vet[c]='12'
			if vet[c].upper()=='D':
				vet[c]='13'
			if vet[c].upper()=='E':
				vet[c]='14'
			if vet[c].upper()=='F':
				vet[c]='15'
	vet=[int(d) for d in vet]
	vet=list(reversed(vet))
	for c in range(len(vet)):
		soma+=vet[c]*(y**c)
	print(soma)

def validar(y):
	e=1
	if y==2:
		while e!=0:
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			vet=[int(d) for d in x]
			for c in range(len(vet)):
				if vet[c] not in (0,1):
					e=1
	if y==8:
		while e!=0:
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			vet=[int(d) for d in x]
			for c in range(len(vet)):
				if vet[c] not in range(8):
					e=1
	if y==16:
		while e!=0:
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			vet=[d for d in x]
			for c in range(len(vet)):
				if vet[c].upper() not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
					e=1
	return x

escolha=0
while escolha not in (1,2):
	escolha=int(input('1 - Decimal para Binario/Octal/Hexadecimal\n2 - Binario/Octal/Hexadecimal para Decimal\nEscolha uma opcao: '))
if escolha==1:
	x=int(input('Digite o numero decimal que deseja converter: '))
	y=0
	while y not in (2,8,16):
		y=int(input('Digite a base para conversao[2,8 ou 16]: '))
	dectobase(x,y)
else:
	y=0
	while y not in (2,8,16):
	    y=int(input('Digite a base que deseja converter para decimal [2,8 ou 16]: '))
	x=validar(y)
	basetodec(x,y)
	