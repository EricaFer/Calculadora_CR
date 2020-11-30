from os import system, name
from time import sleep
import json

def clear(): 
        if name == 'nt': 
            _ = system('cls')

def cleanse(tempo):
        sleep(tempo)
        clear()

def input_ask(tipo,question,estilo = '',definidor = ''):
    
    valid = False

    while not valid:
        try:
            name = tipo(input(question))
            cleanse(3)
            
            if definidor != None:
                if name in definidor:
                    pass
            else:
                pass

        except:
            print('\nResposta inválida, por favor tente novamente')

            if estilo == 'option':
                print('Você escolheu a opção' + name)

            cleanse(3)
    
    return name

def pergunta_init():

    print("Olá, o que gostaria de fazer hoje?\n\n")

    question1 = '1.Prever o CRA desse semestre\n\n2.Calcular quanto tenho que tirar para ter determinado CRA\n\n3.Converter para GPA\n\n4.Sair'
    choice = input(int,question1,'option',[range(0,5)])

    return choice

def choice1():

    question2 = '\nQuantas matérias você puxou esse semestre\n'
    materias_num = input_ask(int,question2)

    question3 = "\nQuantos créditos você puxou esse semestre?\n"
    cred = input_ask(int,question3)

    for i in range(1,materias_num+1):

        question4 = 'Digite o nome da matéria %i\n'%(i)
        nome = input_ask(str,question4)

        question5 = "\nDigite a nota que você espera tirar em %s:\n"%(nome)
        nota = input_ask(float,question5)

        question6 = '\nDigite quantos créditos %s tem:\n'%(nome)
        peso = input_ask(int,question6)
  
        CR_estimado += (nota*peso)/cred
        cleanse(1)

    return(("\n\n\nSeu CR será %i"%(CR_estimado)))

def choice2():

    CRA_atual = 0

    question7 = "\nQuantos créditos você já fez até agora?(sem contar os que ainda estão sendo cursados)\n\n"
    question8 = "\nQual é o seu CRA atualmente?\n\n"
    question9 = "\nQual CRA você quer atingir?\n"
    question10 = "\nEm quanto tempo você deseja atingir esse objetivo?\n"
    question11 = "\nColoque a média de créditos por período\n"

    ct = input_ask(int,question7)
    CRA_atual = input_ask(float, question8)
    alvo = input_ask(float, question9)
    periodos = input_ask(int,question10)
    media = input_ask(float, question11)

    resposta = round(((alvo*periodos*ct) - (ct*float(CRA_atual))/periodos),1)
    cleanse(1)
    return (("\n\n\nVocê precisa tirar %i em %i semestres para ter o CRA %f"%(resposta,periodos,alvo)))

def converter(number):
    number1 =+ 0.3

    letras = ['A','B','C','D','E','F']

    for i in range (0,5):

        if number1//1 == i:
            letter = letras[i]
        
        if number%1 >

    return letter

def choice3():
    question12 = '\nQual o seu CRA atual?'
    CRA = input_ask(float, question12)

    number = round(CRA*(2/5),1)

for _ in range(0,4):
    choice = pergunta_init()
    if choice == 1:
        print(choice1())
    elif choice == 2:
        print(choice2())
    elif choice == 3:
        print(choice3())
    elif choice == 4:
        break



