#--------------------------------------------------------
# Código em Python p/ controle e protese
#MPU6050
# mfelippe.bsb@hotmail.com
#--------------------------------------------------------

import serial

porta_serial = serial.Serial('COM6', 9600);
print("iniciando leitura dos dados seriados")


while(1):
    leitura_serial = str(porta_serial.readline())
    print(leitura_serial[2:-5])

