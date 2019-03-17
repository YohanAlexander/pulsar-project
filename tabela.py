# Importa as bibliotecas
import serial, time, datetime, csv

# Valor lógico que representa a conexão do arduino
connectado = False

# Estabelece a conexão a porta serial do arduino
portas = ['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','COM1', 
'COM2', 'COM3', 'COM4','COM5', 'COM6','COM7', 'COM8', 'COM9','COM10','COM11']

for dispositivo in portas:
    try:
        print("\nConectando... %s" %(dispositivo))
        arduino = serial.Serial(port = dispositivo, baudrate = 9600, timeout = 1)
        break
    except:
        print("Conexão falhou com: %s \n" %(dispositivo))

# Laço até estabelecer a conexão com o arduino
while not connectado:
    porta = arduino.read()
    arduino.flushInput()
    connectado = True
    print("Conectado a porta: %s \n" %(arduino.portstr))

# Decodifica a saída serial do arduino e salva no arquivo csv
while True:
    try:   
        with open('tabela.csv', mode = 'w', newline = '') as tabela:
            while True:
                linha = arduino.readline().decode('utf-8').strip('\r\n')
                tempo = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S.%f')
                arquivo = csv.writer(tabela, delimiter = ",")
                arquivo.writerow([tempo, linha])
    except:
        print("Conexão Interrompida\n")
        break

tabela.close()
arduino.close()