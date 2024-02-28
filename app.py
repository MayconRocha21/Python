# Introdução ao Python

# Variáveis e Tipos de Dados
nome = "Maycon" # Este é dado do tipo String
idade = 35      # Este é um dado do tipo number inteiro - Int
altura = 1.71   # Este é um dado do tipo number Float
estudante = True # Este é um dado do tipo Boolean - True or False

# Saída de dados
print(f'Olá, meu nome é {nome}')
print(f'Eu tenho {idade} anos de idade.')
print(f'Tenho {altura} de altura')

if estudante:
    print("Sou estudante.")
else:
    print("Não sou um estudante")

# Entrada de dados
nome_usuario = input('Qual o seu nome: ')

# Estruturas de controle
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")

# Listas
frutas = ['banana', 'uva', 'melancia', 'morango', 'kiwi', 'laranja']
print(f'Minhas frutas favoritas são {frutas}')

# Tuplas
coordenadas = ('Maycon', 35, 1.71)

#loop (Laço) com for
for contador in range (1,6):
    print("Contagem: ", contador)

contador = 1
while contador <=5:
    print("Contagem: ", contador)
    contador +=1

# Funções
def saudacao(nome):
    return "Olá, " + nome + "!"

mensagem = saudacao("Camilla")
print(mensagem)