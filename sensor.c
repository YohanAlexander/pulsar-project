#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

int ADCsingleREAD(uint8_t adctouse){

    int ADCval;

    ADMUX = adctouse;        // Usa #1 ADC
    ADMUX |= (1 << REFS0);   // Usa AVcc como referência
    ADMUX &= ~(1 << ADLAR);  // Limpa para a resolução de 10 bits
    
    ADCSRA |= (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0); // 128 prescaler para 8Mhz
    ADCSRA |= (1 << ADEN);    // Habilita o ADC
    ADCSRA |= (1 << ADSC);    // Começa a conversão do ADC
    
    while(ADCSRA & (1 << ADSC)); // Espera o ADC terminar

    ADCval = ADCL;
    ADCval = (ADCH << 8) + ADCval; // Concatena os bits mais e menos significativos

    return ADCval;
}

int Sinal;
float Lux;

int main (void){

    Serial.begin(9600); // Velocidade padrão da comunição serial

    while (1){

    Sinal = ADCsingleREAD(0); // Leitura do pino analógico
    Lux = Sinal * 0.9765625; // Conversão para valor de luminosidade
    Serial.println(Lux); // Impressão da luminosidade no serial
    _delay_ms(5); // Aguarda 5 milisegundos
    
    }
}