/*
 * 200729.c
 *
 * Created: 2020-07-29 오전 10:08:32
 * Author : user
 */ 

#define F_CPU 16000000UL
#include "uart.h"

unsigned short read_adc(char ch)
{
	ADMUX = 0x40 | (ch & 0x07);
	_delay_us(50);
	ADCSRA |= 1 << ADSC; 
	while((ADCSRA &(1<<ADIF))== 0);
	return ADCL | (ADCH << 8);
}

int main(void)
{
	unsigned short x = 0, y = 0;
    DDRA = 0xFF;
	DDRF = 0x00;
	ADCSRA = 0x87;
	ADMUX = 0x40;
	
	uart_init(BAUDRATE(9600));
    while (1) 
    {
		x = read_adc(0) * 2 / 1023;
		y = read_adc(1) * 2 / 1023;
		uart_write(0x02);
		uart_write(x + '0');
		uart_write(y + '0');
		uart_write(0x03);
		_delay_ms(100);
    }
}

