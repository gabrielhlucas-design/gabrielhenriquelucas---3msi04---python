print("Bem vindo a Urna Eletrônica - A votação será com 3 candidatos")
def CadastroCandidato():
    n1 = input("Digite o nome do primeiro candidato: ")
    num1=int(input("Digite o número do primeiro candidato: "))
    n2 = input("Digite o nome do segundo candidato: ")
    num2=int(input("Digite o número do segundo candidato: "))
    n3 = input("Digite o nome do terceiro candidato: ")
    num3=int(input("Digite o número do terceiro candidato: "))
    return n1, num1, n2, num2, n3, num3

n1, num1, n2, num2, n3, num3 = CadastroCandidato() #Retira da função
while num1==num2 and num1==num3:
    print("Candidatos iguais, digite novamente!!!")
    CadastroCandidato()
print("Sucesso!!! Candidatos Cadastrados e nenhum numero repetido!")
print("-----Iniciando a Votação ----")
quantidadeVotos = int(input("Digite quantas pessoas irão votar:  "))
