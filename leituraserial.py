#--------------------------------------------------------
# Código em Python p/ controle e protese
#MPU6050
# mfelippe.bsb@hotmail.com
#--------------------------------------------------------

import serial
import matplotlib.pyplot as plt
import numpy as np

porta_serial = serial.Serial('COM6', 9600);
print("iniciando leitura dos dados seriados")

#Array de dados do MPU6050
ACx = []
ACy = []
ACz = []
AGx = []
AGy = []
AGz = []
i=0;
while i<=100: # loop para captar os primeiros 100 dados
    leitura_serial = str(porta_serial.readline())#inicia a leitura serial
    leitura_serial = leitura_serial[2:-5] #remove os caracteris indesejado
    dado = leitura_serial.split(',') #separa os dados
    #print(dado)
    
    #separando os dados do array dado e convertendo p /inteiro

    #adcionando dados no array
    #dados do Aceletrometro  
    ACx.append(float(dado[0]));
    ACy.append(float(dado[1]));
    ACz.append(float(dado[2]));

    #dados do Giroscopio(x,y,z)
    AGx.append(float(dado[3]));
    AGy.append(float(dado[4]));
    AGz.append(float(dado[5]));
    i=i+1;

print(ACx);
print(ACy);
print(ACz);
print(AGx);
print(AGy);
print(AGz);

  
