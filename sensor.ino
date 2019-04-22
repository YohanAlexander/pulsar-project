// Importa as bibliotecas
#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

// Função para regular a taxa de amostragem do conversor A/D
int ADCsingleREAD(uint8_t adctouse){

    int ADCval;

    ADMUX = adctouse;        // Usa #1 ADC
    ADMUX |= (1 << REFS0);   // Usa AVcc como referência
    ADMUX &= ~(1 << ADLAR);  // Limpa para a resolução de 10 bits
    
    ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); // 128 prescalonador para 8Mhz
    ADCSRA |= (1 << ADEN);    // Ativa o ADC
    ADCSRA |= (1 << ADSC);    // Começa a conversão do ADC
    
    while(ADCSRA & (1 << ADSC)); // Espera o ADC terminar

    ADCval = ADCL;
    ADCval = (ADCH << 8) + ADCval; // Concatena os bits mais e menos significativos

    return ADCval;
}

int Sinal; // Leitura do sinal em uma escala de 1024 bits
float Lux; // Luminosidade em uma escala de 0 a 1000 Lux

int main (void){

    Serial.begin(115200); // Velocidade da comunição serial

    while (1){

    Sinal = ADCsingleREAD(0); // Leitura do pino analógico
    Lux = Sinal * 0.9765625; // Conversão para valor de luminosidade
    Serial.println(Lux); // Impressão da luminosidade no serial
    _delay_ms(5); // Aguarda 5 milisegundos
    
    }
}
