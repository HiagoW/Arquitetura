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
			vet=[int(d) for d in x]
			#percorre o vetor
			for c in range(len(vet)):
				#se algum elemento nao for 0 ou 1, variavel e recebe 1 e o usuário deve digitar novamente o numero
				if vet[c] not in (0,1):
					e=1
	if y==8:
		while e!=0:
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			vet=[int(d) for d in x]
			for c in range(len(vet)):
				#mesma validação anterior, mas verifica se os elementos são (0,1,2,3,4,5,6 ou 7)
				if vet[c] not in range(8):
					e=1
	if y==16:
		while e!=0:
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			#neste caso não converte para int, apenas separa os elementos da string
			vet=[d for d in x]
			for c in range(len(vet)):
				#Verifica se o numero na base 16 digitado não contém elementos diferentes dos abaixos
				if vet[c].upper() not in ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'):
					e=1
	return x

escolha=0
#valida se usuario vai escolhar uma das opcoes exibidas
while escolha not in (1,2):
	escolha=int(input('1 - Decimal para Binario/Octal/Hexadecimal\n2 - Binario/Octal/Hexadecimal para Decimal\nEscolha uma opcao: '))
if escolha==1:
	x=int(input('Digite o numero decimal que deseja converter: '))
	y=0
	#valida se usuario vai escolher uma das bases disponiveis
	while y not in (2,8,16):
		y=int(input('Digite a base para conversao[2,8 ou 16]: '))
	dectobase(x,y)
else:
	y=0
	while y not in (2,8,16):
	    y=int(input('Digite a base que deseja converter para decimal [2,8 ou 16]: '))
	x=validar(y)
	basetodec(x,y)
	
>>>>>>> Hiago
