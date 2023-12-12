import os

nomes = []
contas = []
saldo = []
def cadastrar(proprietario,conta):
    limpar()
    contas.append(conta)
    nomes.append(proprietario)
    saldo.append(0)
    return "Conta cadastrada!"
def deposito(num):
    nom = float(input("Valor que deseja depositar:"))
    if num in contas:
        posicao = contas.index(num)
        saldo[posicao] = (saldo[posicao]) + nom
        return "Deposito feito com sucesso!"
def pesquisar():
    limpar()
    cont = 0
    while cont < len(contas):
      print("Nomes:", nomes[cont],"\t", "Número:",contas[cont], "\t", "Saldo:", "R$",saldo[cont])
      cont += 1
def limpar():
    os.system('cls')

def sacar(nuk):
    nuk = float(input("Valor que deseja sacar:"))
    if num in contas:
        posicao = contas.index(num)
        saldo[posicao] = (saldo[posicao]) - nuk
        return "Saque feito com sucesso!"
def transferir():
    tr = float(input("Sua conta:"))
    tr2 = float(input("Conta do destinatário:"))
    val = float(input("Valor que deseja tansferir:"))
    tri = contas.index(tr)
    tr23 = contas.index(tr2)
    
    if saldo[tri] < val:
        print("Saldo não encontrado")
    saldo[tri] -= val
    saldo[tr23] += val 
    return "Transferência feita com sucesso!"
op = 10
while op != 0:
    op = int(input("\n 1 - Cadastrar sua conta"+
                   "\n 2 - Pesquisar"+
                   "\n 3 - Deposite"+
                   "\n 4 - Sacar"+
                   "\n 5 - Transferir"+
                   "\n 0 - Feche o sistema"+
                   "\n Digite sua opção: "))
    if op == 1:
        limpar()
        num = int(input("Número da conta:"))
        nome = input("Seu nome:")
        print(cadastrar(nome, num ))
    elif op == 2:
        pesquisar()
    elif op == 3:
        limpar()
        valor = int(input("Número da conta:"))
        print(deposito(valor))
    elif op == 4:
        sas = float(input("Número da conta:"))
        print(sacar(sas))
    elif op == 5:
        transfer()