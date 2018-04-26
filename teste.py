from array import array
def func(x, y):
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
	print(vet)
	vet=[int(d) for d in vet]
	vet=list(reversed(vet))
	for c in range(len(vet)):
		soma+=vet[c]*(y**c)
		print(vet[c],'*(',y,'**',c)
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

y=0
while y not in (2,8,16):
    y=int(input('Digite a base para conversao[2,8 ou 16]'))
x=validar(y)

func(x,y)