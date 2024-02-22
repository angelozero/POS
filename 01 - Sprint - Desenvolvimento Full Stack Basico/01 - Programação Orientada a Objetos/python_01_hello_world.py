# imprimindo uma mensagem
print("Hello World!")
print("")

# declaracao de variaveis
uma_string = "Angelo"
um_inteiro = 10
um_float = 7.584
um_booleano = True

# impressao das variaveis
print(uma_string)
print(um_inteiro)

# operacao aritmetica
resultado_1 = 7 + 5
resultado_2 = 2 * 2

# imprime resultado de operacoes aritimeticas
print("Restulado da soma: " + str(resultado_1))
print("Restulado da mult: " + str(resultado_2))
print("")

# usando operadores de igualdade
print("um e igual a um       ? - " + str(1 == 1))
print("dois e menor que a um ? - " + str(2 < 1))
print("dois e diferente de um? - " + str(2 != 1))
print("")

# declarando uma lista
lista_de_numeros = [1,2,3,4] 
print("isso e uma lista de numeros" + str(lista_de_numeros))
lista_de_numeros.append(5)
print("a lista de numeros recebeu um novo valor" + str(lista_de_numeros))
print("")

# declarando uma tupla
tupla = ('copa','ouro','espada','pau')
print("isso e uma tupla" + str(tupla))
print("")

# declarando um dicionario
notas = {"Angelo": 10, "Jake": 12}
print("imprimindo o dicionario " + str(notas))
print("o aluno Jake esta no dicionario? " + str("Jake" in notas))
print("")

# condicoes if, elif e else
nome = "Angelo"
idade = 33

if nome == "Jake":
    print("o nome encontrado e Jake")
    print("a idade de jake é " + str(idade))
elif nome == "Teste":
    print("o nome encontrado e Teste")
    print("teste nao tem idade")
else:
    print("o nome encontrado foi " + str(nome))
    print("a idade dé " + str(nome) + " é " + str(idade)) 
print("")

# loops for, while, break
for i in range(5):
    print("valor em loop " + str(i))
print("")
    
valor_fim_while = 0
while valor_fim_while <= 3:
    print("o valor " + str(valor_fim_while) + " ainda e menor ou igual a 3")
    valor_fim_while += 1
print("")

valor_fim_while_break = 0
while valor_fim_while_break < 5:
    if valor_fim_while_break == 3:
        print("valor while com break é igual a 3, fim da execucao")
        break
    valor_fim_while_break += 1
    print("valor while com break é " + str(valor_fim_while_break))
print("")

# declarando funcoes
def hello_world():
    print("funcao hello_world() foi invocada")
    
hello_world()
print("")

def func_com_parametro(nome):
    print("o nome passado para a funcao é " + str(nome))
    
func_com_parametro("Jake")
print("")

def func_soma_com_retorno(a, b):
    return a + b

soma_da_func = func_soma_com_retorno(2, 2)

print("o resultado da funcao func_soma_com_retorno é " + str(soma_da_func))
print("")

def func_com_valor_default(nome, sobrenome="Ferreira"):
    return nome + " " + sobrenome

print("Nome sem passar sobrenome " + str(func_com_valor_default("Angelo")))
print("Nome  passando  sobrenome " + str(func_com_valor_default("Angelo", "Lorann")))
print("")
