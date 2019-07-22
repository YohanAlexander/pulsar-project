#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Importa as bibliotecas

# Generic/Built-in
import time, csv, sys, os

# Other Libs
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import pandas as pd
import tqdm

# Wrapping Header
__author__ = 'Yohan Alexander'
__copyright__ = 'Copyright 2019, Pulsar Project' 
__credits__ = ['Yohan Alexander']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Yohan Alexander'
__email__ = 'yohanfranca@gmail.com'
__status__ = 'Dev'

def main(args):

    print("\n###########################\n\nSimulated Pulsar LightCurve\n\n###########################\n")

    # Valor lógico que representa a conexão do arduino
    conectado = False

    # Valor de referência para contagem do tempo de exposição
    timeout = 0    

    # Tempo de exposição para captura dos dados
    while(True):
        try:
            expo = int(input(">>> Tempo para captura dos dados em segundos: \n")) * 100
            if type(expo) != int:
                raise Exception
            break
        except:
            print(">>> Valor Inválido\n")
            continue
    
    # Nome do arquivo de saída
    while(True):
        try:
            dados = input(">>> Nome do arquivo de saída: \n")
            if len(dados) == 0:
                raise Exception
            break
        except:
            print(">>> Valor Inválido\n")
            continue
        
    # Título do gráfico de saída
    while(True):
        try:
            title = input(">>> Título que será exibido no gráfico: \n")
            if len(title) == 0:
                raise Exception
            break
        except:
            print(">>> Valor Inválido\n")
            continue

    # Tamanho da fatia dos dados para plotar no gráfico
    while(True):
        try:
            plot = int(input(">>> Fatia dos dados que será plotada no gráfico: \n"))
            if type(plot) != int:
                raise Exception
            break
        except:
            print(">>> Valor Inválido\n")
            continue
    
    # Caminho da porta serial do arduino
    print('>>> Procurando dispositivos...\n')
    porta = list(serial.tools.list_ports.comports(include_links=False))
    
    # Estabelece a conexão com a porta serial do arduino    
    if(len(porta) > 0):
        for dispositivo in porta:
            try:
                print(">>> Conectando... %s\n" %(dispositivo.device))
                arduino = serial.Serial(port = dispositivo.device, baudrate = 115200, timeout = 1)
                if arduino.isOpen():
                    conectado = True
                break
            except:
                print(">>> Conexão falhou com: %s\n" %(dispositivo.device))
    else:
        print(">>> Nenhum dispositivo encontrado\n")
    
    # Condição até estabelecer a conexão com o arduino
    if conectado == True:
        porta = arduino.read()
        arduino.flushInput()
        arduino.flushOutput()
        print(">>> Conectado a porta: %s\n" %(arduino.portstr))
    else:
        print(">>> Verifique a conexão e reinicie o programa\n")
        quit(main(args[0]))
    
    # Tempo inicial de referência
    tzero = int(round(time.time() * 1000))

    # Decodifica a saída serial do arduino e salva no arquivo csv
    while timeout < expo:
        try:
            with open('%s.csv' %dados, mode = 'w', newline = '') as tabela:
                print(">>> Capturando dados...\n")
                for i in tqdm(range(expo)):
                    linha = arduino.readline().decode('utf-8').strip('\r\n')
                    tempo = int(round(time.time() * 1000)) - tzero
                    arquivo = csv.writer(tabela, delimiter = ",")
                    arquivo.writerow([tempo, linha])
                    timeout += 1
                print(">>> Dados obtidos com sucesso\n")
        except:
            print(">>> Conexão Interrompida\n")
            quit(main(args[0]))

    tabela.close()
    arduino.close()

    try:
        # Plota os dados obtidos no gráfico e salva a imagem obtida
        df = pd.read_csv('%s.csv' %dados, delimiter=',')
        df.columns=['Tempo', 'Luminosidade']
        df[:plot].plot.line(x='Tempo', y='Luminosidade', figsize=(20,10))

        # Formata a saída do gráfico e a legenda da imagem
        plt.title('%s' %title)
        plt.xlabel('Tempo (milisegundos)')
        plt.ylabel('Luminosidade (lux)')
        plt.savefig('%s.png' %dados, bbox_inches='tight')

        print(">>> Imagem salva em %s.png\n" %dados)

    except:
        print(">>> Erro ao gerar a imagem\n")
        quit(main(args[0]))
    
if __name__ == "__main__":
    main(sys.argv)
