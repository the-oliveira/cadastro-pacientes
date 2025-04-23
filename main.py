import modules as md
from time import sleep
import pandas as pd

print("="*40)
print(f"{'CADASTRO DE PACIENTES':^40}")
print("="*40)

#Carregar o arquivo com os dados salvos
df = pd.read_csv("pacientes.csv")

while True:
    sleep(5)
    print(f"{'MENU PRINCIPAL':^40}")
    print("="*40) 
    print("[ 1 ] Cadastrar novo paciente")
    print("[ 2 ] Consultar ou Atualizar status do paciente")
    print("[ 3 ] Sair do Aplicativo")   
    print("="*40)  
    sleep(2)
    
    escolhaUsuario = input("Opção desejada: ")[0] #Coletar escolha do usuario
    while escolhaUsuario not in '123': #Controle para que a opção seja válida
        escolhaUsuario = input("[ ERRO ] Opção Inválida! ")[0]

    if int(escolhaUsuario) == 1:
        #caminho para adicionar novo paciente

        novoP = md.coletarDados() #Coletar dados para cadastrar
        cadastrarP = md.cadastrarPaciente(novoP) #Cadastro de paciente
        sleep(2)
        print("Voltando para o menu principal...")
        sleep(2)

    elif int(escolhaUsuario) == 2:
        #Caminho para consultar obras e atualizar status
        print('teste 2')
    
    elif int(escolhaUsuario) == 3:
        #Caminho para sair do aplicativo
        print("Encerrando aplicativo")
        print("="*30)
        sleep(3)
        break
