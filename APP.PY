import requests
import time
import os

class colors:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    end = '\033[0m'
    green = '\033[92m'
    red = '\033[1;91m'

def titulo_principal():
    print('-'*37)
    print(colors.cyan + 'TERMINAL PARA CONVERSÃO DE MOEDAS' + colors.end)
    print('-'*37)

def verifica_opcao_selecionada(moeda):

    if moeda == '1':
        moeda = 'USD'
    elif moeda == '2':
        moeda = 'BRL'
    elif moeda == '3':
        moeda=input('Certo, digite o código da moeda:')
    return moeda

def msg_e_selecao_de_moeda(msg):

    verificando_selecao=False
    while verificando_selecao == False:

        print(f'{msg}:\n')
        moeda_usuario = input('[1] - USD - Dólar Americano\n[2] - BRL - Real Brasileiro\n[3] - Outra moeda\n\nDigite a opção desejada:' )
        if moeda_usuario not in ('1','2','3'):
            print(colors.red + 'SÃO ACEITOS SOMENTE OS VALORES 1,2 ou 3' + colors.end + os.linesep)
            time.sleep(2)
            verificando_selecao=False
        else:
            return moeda_usuario

def sleep_selecionando_moeda():
    print('Ok, seleconando moeda...\n')
    time.sleep(2)

def escolha_da_primeira_moeda():

    moeda_usuario= msg_e_selecao_de_moeda('Escolha a PRIMEIRA moeda:')
    primeira_moeda_usuario = verifica_opcao_selecionada(moeda_usuario)
    sleep_selecionando_moeda()
    return primeira_moeda_usuario

def escolha_da_segunda_moeda():

    moeda_usuario= msg_e_selecao_de_moeda('Escolha a SEGUNDA moeda:')
    segunda_moeda_usuario = verifica_opcao_selecionada(moeda_usuario)
    sleep_selecionando_moeda()

    return segunda_moeda_usuario

def recebe_dados_api(primeira_moeda_usuario,segunda_moeda_usuario):

    resultado_get = requests.get(f'https://economia.awesomeapi.com.br/last/{primeira_moeda_usuario}-{segunda_moeda_usuario}') 
    result_json=resultado_get.json()
    valor_da_escolha = float(result_json[f'{primeira_moeda_usuario}{segunda_moeda_usuario}']['high'])
    print(f'1 {primeira_moeda_usuario} = {valor_da_escolha} {segunda_moeda_usuario}')
    return valor_da_escolha

def calculo_da_conversao(valor_da_escolha):
    valor_usuario_conversao = float(input('Qual valor que você deseja converter?'))
    conversao_inicial = valor_da_escolha*valor_usuario_conversao
    conversao_final = round(conversao_inicial,2)
    print(colors.green + 'Convertendo....' + colors.end)
    time.sleep(2)
    print(f'{colors.yellow}RESULTADO =  {colors.end} {valor_usuario_conversao} {primeira_moeda_usuario} =  {conversao_final} {segunda_moeda_usuario}\n')


###  CODE MAIN #####################################################

titulo_principal()
valida_code_main = False
while valida_code_main == False:
    primeira_moeda_usuario = escolha_da_primeira_moeda()
    segunda_moeda_usuario = escolha_da_segunda_moeda()
    try:
        valor_da_escolha = recebe_dados_api(primeira_moeda_usuario,segunda_moeda_usuario)
        calculo_da_conversao(valor_da_escolha)
    except KeyError as KeyError:
        print(colors.green + 'MOEDA INSERIDA INCORRETAMENTE - REFAÇA TODO O PROCESSO' + colors.end + os.linesp) 
       
    
