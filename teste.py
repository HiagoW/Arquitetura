from array import array
def func(x, y):
	soma=0
	vet=[int(d) for d in x]
	vet=list(reversed(vet))
	for c in range(len(vet)):
		soma+=vet[c]*(y**c)
		print(vet[c],'*(',y,'**',c)
	print(soma)
y=0
while y not in (2,8,16):
    y=int(input('Digite a base para conversao[2,8 ou 16]'))
x=input('Digite o numero que deseja converter para decimal: ')
func(x,y)