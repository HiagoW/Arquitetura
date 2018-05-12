def dectobase(x, y):
    #cria vetor que vai receber o numero na outra base
    vet=[]
    c=0
    #vai dividindo o numero decimal na base escolhida até chegar a zero
    #atribuindo o resto da divisao a variavel i
    while x>0:
        i=x%y
        #se a base for 16, e o resto for um dos numeros maiores que 9, atribui a letra correspondente
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
        #adiciona o resto da divisão no final do vetor
        vet.append(i)
        #x recebe o resultado da divisão inteiro de x por y
        x=x//y
        #contador c recebe +1 para saber o tamanho do vetor
        c+=1
    #inverte o vetor para exibir o numero na ordem correta    
    vet.reverse()
    #sabendo o tamanho do vetor na variavel c, exibe cada elemento
    for i in range(c):
        print(vet[i], end="")

def basetodec(x, y):
	vet=[]
	soma=0
	#se a base escolhida for 16...
	if y==16:
		#cria um vetor separando todos elementos da string que o usuário digitou
		vet=[d for d in x]
		#percorre os elementos e para cada letra, troca pelo número correspondente
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
		#converte os numeros substituidos para inteiro
		vet=[int(d) for d in vet]
	else:
		#se a base não for 16, converte diretamente todos elementos para inteiro
		vet=[int(d) for d in x]
	#inverte a ordem do vetor
	vet=list(reversed(vet))
	for c in range(len(vet)):
		#a variavel soma recebe a soma dos elementos do vetor, multiplicado pela base escolhida elevada a posição correspondente
		#ex: base 2 - 011 = 1*2^0 + 1*2^1 + 0*2^2
		soma+=vet[c]*(y**c)
	print(soma)

def validar(y):
	e=1
	#valida o numero na base 2
	if y==2:
		while e!=0:
			#e recebe 0, se tiver algo errado no numero, vai receber 1 e continuar no while
			e=0
			x=input('Digite o numero que deseja converter para decimal: ')
			#cria um vetor separando a string x e convertendo todos elementos em inteiros
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
	