<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/yohanalexander/pulsar-project">
    <img src="pulsar.png" alt="Logo" width="50%" height="50%">
  </a>

  <h1 align="center">Pulsar Simulado</h1>

  <p align="center">
    Visualização de dados por comunicação serial!
    <br />
   
<!-- ABOUT THE PROJECT -->
## Sobre o projeto


O projeto foi construído para o desenvolvimento de habilidades técnicas no uso de programação para o processamento de sinais. 

O software faz uso de comunicação serial via Arduino para visualização de dados obtidos por um sensor de luminosidade. 

O sinal obtido é lido, armazenado e processado em tempo real com uso de bibliotecas para a plotagem gráfica de uma curva de luz, ou seja intensidade luminosa em função do tempo, em uma interface interativa.

<!-- GETTING STARTED -->
## Funcionamento

### Pré-requisitos
A versão do interpretador `Python` utilizada no desenvolvimento foi a `3.6`, por isso para o funcionamento adequado é necessária uma distribuição acima desta versão, que pode ser gerenciada em ambientes virtuais como o `Anaconda`.

Além disso é necessário ter instalada a `IDE` do `Arduino` para instalação dos drivers adequados para as placas, e gerenciamento das portas de comunicação serial.

* Python>=3.6 
* Arduino IDE

Em  sistemas linux utilize a linha de comando:

```sh
sudo apt install python3
sudo apt install arduino
```

Para executar o software corretamente, você precisará de algumas dependências que podem ser gerenciadas pelo gerenciador de pacotes do Python `PIP`, use o comando no terminal:

```sh
pip install -r requirements.txt
```

### Compilação

Para compilar a sketch `sensor.ino` do programa e gravá-la no bootloader da placa, use a `IDE` do `Arduino`.

<!-- USAGE EXAMPLES -->
### Uso
Para iniciar a interface do software basta executar o comando:
```sh
python pulsar.py
```

