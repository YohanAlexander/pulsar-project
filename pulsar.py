#!~/anaconda3/bin/python
# -*- coding: utf-8 -*-

# Importa as bibliotecas
# Generic/Built-in
import serial, time, csv, sys
import matplotlib.pyplot as plt
import pandas as pd

__author__ = 'Yohan Alexander'
__copyright__ = 'Copyright 2019, Pulsar Project' 
__credits__ = ['Yohan Alexander']
__license__ = 'MPL 2.0'
__version__ = '0.1.0'
__maintainer__ = 'Yohan Alexander'
__email__ = 'yohanfranca@gmail.com'
__status__ = 'Dev'

# Estilo de plotagem do gráfico
plt.style.use('fivethirtyeight')

def main(args):

    # Valor lógico que representa a conexão do arduino
    conectado = False

    # Caminho da porta serial do arduino
    porta = list()
    porta.append(args[1])

    # Tempo de exposição para captura dos dados
    expo = int(args[2]) * 100
    timeout = 0

    # Nome do arquivo de saída
    dados = args[3]

     # Estabelece a conexão com a porta serial do arduino
    for dispositivo in porta:
        try:
            print("\nConectando... %s" %(dispositivo))
            arduino = serial.Serial(port = dispositivo, baudrate = 115200, timeout = 1)
            break
        except:
            print("Conexão falhou com: %s \n" %(dispositivo))

    # Laço até estabelecer a conexão com o arduino
    while not conectado:
        porta = arduino.read()
        arduino.flushInput()
        conectado = True
        print("Conectado a porta: %s \n" %(arduino.portstr))
    
    # Tempo inicial de referência
    tzero = int(round(time.time() * 1000))

    # Decodifica a saída serial do arduino e salva no arquivo csv
    while timeout < expo:
        try:
            with open('%s.csv' %dados, mode = 'w', newline = '') as tabela:
                print("Capturando dados...")
                while timeout < expo:
                    linha = arduino.readline().decode('utf-8').strip('\r\n')
                    tempo = int(round(time.time() * 1000)) - tzero
                    arquivo = csv.writer(tabela, delimiter = ",")
                    arquivo.writerow([tempo, linha])
                    timeout += 1
                print("Dados obtidos com sucesso\n")
        except:
            print("Conexão Interrompida\n")
            break

    tabela.close()
    arduino.close()

    # Plota os dados obtidos no gráfico e salva a imagem obtida
    df = pd.read_csv('%s.csv' %dados, delimiter=',')
    df.columns=['Tempo', 'Luminosidade']
    df[50:500].plot.line(x='Tempo', y='Luminosidade', figsize=(20,10))
    
    # Formata a saída do gráfico e a legenda da imagem
    plt.title('%s' %dados)
    plt.xlabel('Tempo (milisegundos)')
    plt.ylabel('Luminosidade (lux)')
    plt.savefig('%s.png' %dados, bbox_inches='tight')

    print("Imagem salva em %s.png\n" %dados)
    
if __name__ == "__main__":
    main(sys.argv)