#Password generator by Nabha

# gera senha de apenas numeros
# numeros e letras
# numeros, letras e caracteres especiais
# numeros, letras, caracteres especiais e maiusculas
versao=0.0

import random
import os
from time import sleep

#DETECTANDO SISTEMA OPERACIONAL

if (os.name == 'posix'):
    def limpartela():
        os.system('clear')
else:
    def limpartela():
        os.system('cls')

def mostraMenu():
    limpartela()
    print(f'Gerador de Senha by Nabha versão {versao}')
    print('0- Encerrar gerador de senha')
    print('1- Gera uma senha numérica aleatória não sequencial de tamanho especificado')
    print('2- Gera senha alfabética')
    print('3- Gera senha numerica e alfabetica')
    print('4- Gera senha numérica, alfabética e com caractéres especiais.')
    print('??- Em breve...')
    escolha = int(input("Insira sua escolha:\n"))
    return escolha

def getSenhaNumOnly():
    digitos=int(input("Quantos dígitos a senha precisa ter?"))
    senha=[]
    b=0
    for x in range(digitos):
        a=random.randrange(0,10)
        while a == b+1 or a == b:
            a=random.randrange(0,10)
        b = a  
        senha.append(a)  
    return senha

def getSenhaAlfabeticaOnly():
    senha=[]
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digitos=int(input("Quantos dígitos a senha precisa ter?")) 
    for x in range(digitos):
        senha.append(alfabeto[random.randrange(len(alfabeto))])    
    return senha

def getSenhaNumAndAlfabetica():
    senha=[]
    digitos=int(input("Quantos dígitos a senha precisa ter?"))
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros=['0','1','2','3','4','5','6','7','8','9']
    for x in range(digitos):
        seletor = random.randint(0,1)
        if (seletor == 0):
            senha.append(alfabeto[random.randrange(len(alfabeto))])
        if (seletor == 1):
            senha.append(numeros[random.randrange(len(numeros))])
    return(senha)

def getSenhaMix():
    senha=[]
    digitos=int(input("Quantos dígitos a senha precisa ter?"))
    alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros=['0','1','2','3','4','5','6','7','8','9']
    chars=['!','@','#','$','%','*','?']
    for x in range(digitos):
        seletor = random.randint(0,100)
        if (seletor < 60):
            senha.append(alfabeto[random.randrange(len(alfabeto))])
        if (seletor >59 and seletor <85):
            senha.append(numeros[random.randrange(len(numeros))])
        if (seletor >84):
            senha.append(chars[random.randrange(len(chars))])
    return senha

def stringToList(a):
    convertido =''.join(str(x) for x in a)
    return convertido

#APLICAÇÃO
rodando= True
while rodando == True:
    escolha= mostraMenu()
    if (escolha == 0):
        print("Gerador encerrado!")
        rodando= False
    if (escolha == 1):
        senha = getSenhaNumOnly()
    if (escolha == 2):
        senha = getSenhaAlfabeticaOnly()
    if (escolha == 3):
        senha = getSenhaNumAndAlfabetica()
    if (escolha == 4):
        senha= getSenhaMix()   

        
senha= stringToList(senha)
print(senha)

