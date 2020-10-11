from os import system, name
from time import sleep

def clear(): 
        if name == 'nt': 
            _ = system('cls')

def cleanse(tempo):
        sleep(tempo)
        clear()

def question():
    print("Olá, o que gostaria de fazer hoje?\n\n")
    choice = input('\n1.Prever o CRA desse semestre\n2.Calcular quanto tenho que tirar para ter determinado CRA\n3.Sair\n\n')
    choice = int(choice)
    print("\nVocê escolheu a opção %i "%(choice))

    return choice

def choice1():
    materias_num = input("\nQuantas matérias você puxou esse semestre\n")
    materias_num = int(materias_num)
    cred = input("\nQuantos créditos você puxou esse semestre?\n")
    cred = int(cred)
    cleanse(1)
    for i in range(1,materias_num+1):
        nome = input("\nDigite o nome da matéria %i\n"%(i))
        nota = input("\nDigite a nota que você espera tirar em %s:\n"%(nome))
        nota = float(nota)
        peso = input("\nDigite quantos créditos %s tem:\n" %(nome))
        peso = int(peso)
        CR_estimado += (nota*peso)/cred
        cleanse(1)
    return(("\n\n\nSeu CR será %i"%(CR_estimado)))

def choice2():
    CRA_atual = 0
    ct = input("\nQuantos créditos você já fez até agora?(sem contar os que ainda estão sendo cursados)\n\n")
    CRA_atual = input("\nQual é o seu CRA atualmente?\n\n")
    alvo = input("\nQual CRA você quer atingir?\n")
    periodos = input("\nEm quanto tempo você deseja atingir esse objetivo?\n")
    choice2 = input("\nColoque a média de créditos por período\n")
    choice2 = int(choice2)
    alvo = float(alvo)
    periodos = int(periodos)
    resposta = round(((alvo*periodos*ct) - (ct*float(CRA_atual))/periodos),1)
    cleanse(1)
    return (("\n\n\nVocê precisa tirar %i em %i semestres para ter o CRA %f"%(resposta,periodos,alvo)))

for _ in range(4):
    choice = question()
    if choice == 1:
        print(choice1())
    if choice == 2:
        print(choice2())
    else:
        break




