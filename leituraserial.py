# --------------------------------------------------------
# Código em Python p/ controle e protese
# MPU6050
# mfelippe.bsb@hotmail.com
# --------------------------------------------------------
from typing import List

import serial
import matplotlib.pyplot as plt
import numpy as np

porta_serial = serial.Serial('COM6', 9600);
print("iniciando leitura dos dados seriados")
#base para plotagem


# Array de dados do MPU6050
pitch_x = []
roll_y = []
yaw_z = []

i = 0;
while i < 1000:  # loop para captar os primeiros 1000 dados
    leitura_serial = str(porta_serial.readline())  # inicia a leitura serial
    leitura_serial = leitura_serial[2:-5]  # remove os caracteris indesejado
    leitura_serial = leitura_serial.split(',')  # separa os dados
    print(leitura_serial)
    i = i + 1

    if i > 60:
        # separando os dados do array dado e convertendo p /inteiro

        # adcionando dados no array
        pitch_x.append(float(leitura_serial[0]))
        roll_y.append(float(leitura_serial[1]))
        yaw_z.append(float(leitura_serial[2]))

plt.plot(pitch_x)
plt.plot(roll_y)
plt.plot(yaw_z)
plt.grid()
plt.show()

print(pitch_x)
print(roll_y)
print(yaw_z)