'''
Exercício 1: LISTA

Dada a lista L= [5, 7, 2, 9, 4,1, 3],escreva um programa que imprima as seguintes informações:

a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos dalista.
e)lista em ordem crescente.
f) lista em ordem decrescente.

Gere uma lista de contendo os múltiplos de 3 entre 1 e50.
'''
print("\n------------------------------------------\n")

L = [5, 7, 2, 9, 4, 1, 3]

print("Lista ",L)
print("Tamanho ",len(L))
print("Maior ", max(L))
print("Menor ", min(L))
print("Soma ", sum(L))
L.sort()
print("Ordem crescente", L)
L.reverse()
print("Ordem crescente", L)

print("\n------------------------------------------\n")

Lista = list(range(3,50,3))
print(Lista)


print("\n------------------------------------------\n")

'''
Exercício 2: Dicionário

Dada a tabela a seguir, crie um dicionário que a represente:    	

João 	     4.50 	
Leandro 	 6.50 	
Sueli 	     3.00 	
Regina 		 8.50 	
Douglas  	10.00 	

Considere um dicionário com 5 nomes de 
alunos e suas notas. Escreva um programa 
que calcule a média dessas notas. 

'''

turma = {'João': 4.50, 'Leandro':6.50, 'Sueli':3.00, 'Regina':8.50, 'Douglas':10.00}
notas = turma.values()
print(notas)
media = sum(notas)/len(notas)
print("Média turma: ", media)

print("\n------------------------------------------\n")

turma2 = {'João': 4.50, 'Leandro':6.50, 'Sueli':3.00, 'Regina':8.50, 'Douglas':10.00}
for chave in turma2:
    print('Chave: {}'.format(chave))

print("\n------------------------------------------\n")

turma2 = {'João': 4.50, 'Leandro':6.50, 'Sueli':3.00, 'Regina':8.50, 'Douglas':10.00}
for valor in turma2.values():
    print('Valor: {:.2f}'.format(valor))

print("\n------------------------------------------\n")

soma = 0
qtd = 0

turma2 = {'João': 4.50, 'Leandro':6.50, 'Sueli':3.00, 'Regina':8.50, 'Douglas':10.00}
for valor in turma2.values():
    print('Valor: {:.2f}'.format(valor))
    soma = soma + valor
    print('Soma das notas: {:.2f}'.format(soma))
    qtd = qtd + 1
    print('Quantidade de Alunos: {}'.format(qtd))

media = soma/qtd
print('Media {:.2f}'.format(media))


'''
Exercício 2: Dicionário

Escreva uma função contador que recebe uma string e devolve
um dicionário. A string só contém palavras em minúsculas,
separadas por espaços e sem pontuação. O dicionário indica
quantas ocorrências de cada palavra existem na string.

Por exemplo:
contador('esse exercício é um exercício fácil ou difícil')
Retorna:
{'é': 1, 'difícil': 1, 'esse': 1, 'ou': 1, 'um': 1, 'fácil': 1, 'exercício': 2}

Já...
contador('o doce perguntou ao doce qual é o doce mais doce e o doce
respondeu ao doce que o doce mais doce é o doce de batata doce')
Retorna o que???
'''

print("\n------------------------------------------\n")

contador = 'esse exercício é um exercício fácil ou difícil'
valor_string = 0
for i in contador:
    valor_string = valor_string + 1
    print(i, end=' ')
    print(valor_string, end=' ') 

print("\n------------------------------------------\n")

contador = 'esse exercício é um exercício fácil ou difícil'
valor_string = 0
for i in contador:
    if (i == i):
        valor_string = valor_string + 1
        print(i, end=' ')
        print(valor_string, end=' ') 