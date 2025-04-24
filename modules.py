from time import sleep
import pandas as pd

def verificarCadastro(nome):
    df = pd.read_csv("pacientes.csv")
    if df.isin([nome]).any().any() == True:
        #Valor já existe no documento
        print("[AVISO] Usuario já possui cadastro!")
        sleep(3)
        
        #aprimorar o código depois para adicionar mais exames em um paciente cadastrado ou algo do tipo
        return True
    else:
         return False

def coletarDados():
    #Função para cadastrar dados do paciente
    nomePaciente = input("Nome Completo: ").capitalize()
    verificar = verificarCadastro(nomePaciente) #Chamar a função para verificar se o paciente já possui registro
    
    if verificar == True:
        print("Paciente já cadastrado... retornando")
    else:
        sexoP = input("Sexo [M/F]: ")[0].upper() #Sexo paciente
        while sexoP not in "MF":
            sexoP = input("[ALERTA] Digite um valor válido [M/F] ")[0].upper()

        
        idadeP = input("Idade: ")
        while int(idadeP) < 0 and int(idadeP) > 120: #Idade paciente
            idadeP = int(input("[ALERTA] Digite uma idade válida "))


        rgP = input("RG: ") #RG paciente
        while len(rgP) < 9 and len(rgP) > 9:
            rgP = input("[ALERTA] Digite um RG válido: ")


        #Trecho para adicionar a lista de exames
        listaExames = []
        while True:
            exameP = input("Exame: ")
            listaExames.append(exameP)
            addEx = input("Deseja adicionar mais exames? ")[0].upper()
            if addEx == 'N':
                break

        statusP = 0 #Padrão de status 0 pois é um cadastro novo

        dadosPaciente = {"nome":nomePaciente, "sexo":sexoP, "idade":idadeP,"rg":rgP, "exames":listaExames, "status":statusP} #dict dados do paciente

        return dadosPaciente


def cadastrarPaciente(dados):
    
    dadosFinais = pd.DataFrame([dados]) #Criando dataframe com os dados do paciente
    dadosFinais.to_csv('pacientes.csv', mode='a', index=False, header=False) #registrando os dados no excel

    print("="*40)
    print(f"{'Cadastro realizado com sucesso!':^30}")
    print("="*40)

    return 200

def consultarPaciente(df, rg):
    if df.isin([rg]).any().any() == True:
        #Valor existe no documento
        print("[AVISO] Cadastro encontrado, selecione a opção: ")
        sleep(3)
        while True:
            print("="*40)
            print("[1] - Consultar exames do paciente")
            print("[2] - alterar status do paciente")
            print("[3] - Voltar ao menu principal")
            print("="*40)
            
            escolha = input("Escolha uma opção: ")
            while escolha not in "123":
                escolha = input("Escolha uma opção: ")

            if escolha == 1:
                print("Caminho para consultar exames")
            
            elif escolha == 2:
                print("Caminho para alterar status")

            else:
                print("Retornando ao menu principal...")
                sleep(2)
                break
        
        return True
    else:
         return False