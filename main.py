# import argparse
import os
import math

KB = 1024
MB = math.pow(1024, 2)
GB = math.pow(1024, 3)

BLOCK_HEADER = 100
BLOCK_SIZE = KB # 10 bytes
TINYTEXT = 256 # 256 bytes
TEXT = 64 * KB # 64 kilobytes
MEDIUMTEXT = 16 * MB # 16 Megabytes
LONGTEXT = 4 * GB # 4 Gigabytes
TINYBLOB = 256
BLOB = 64 * KB
MEDIUMBLOB = 16 * MB
LONGBLOB = 4 * GB
TINYINT = 1
SMALLINT = 2
MEDIUMINT = 3
INT = 4
BIGINT = 8
FLOAT = 4
DOUBLE = 8
REAL = 8
HEADER = 1
CHAR = 1
VARCHAR = 1
MYSQL_SIZE = 3

def CalcularColumna(tipo:str, size:int):
    if(tipo == "TINYTEXT"):
        return TINYTEXT * size + HEADER
    elif(tipo == "TEXT"):
        return TEXT * size + HEADER
    elif(tipo == "MEDIUMTEXT"):
        return MEDIUMTEXT * size + HEADER
    elif(tipo == "LONGTEXT"):
        return LONGTEXT * size + HEADER
    elif(tipo == "TINYBLOB"):
        return TINYBLOB * size + HEADER
    elif(tipo == "BLOB"):
        return BLOB * size + HEADER
    elif(tipo == "MEDIUMBLOB"):
        return MEDIUMBLOB * size + HEADER
    elif(tipo == "LONGBLOB"):
        return LONGBLOB * size + HEADER
    elif(tipo == "TINYINT"):
        return TINYINT * size + HEADER
    elif(tipo == "SMALLINT"):
        return SMALLINT * size + HEADER
    elif(tipo == "MEDIUMINT"):
        return MEDIUMINT * size + HEADER
    elif(tipo == "INT"):
        return INT * size + HEADER
    elif(tipo == "BIGINT"):
        return BIGINT * size + HEADER
    elif(tipo == "FLOAT"):
        return FLOAT * size + HEADER
    elif(tipo == "DOUBLE"):
        return DOUBLE * size + HEADER
    elif(tipo == "REAL"):
        return REAL * size + HEADER
    elif(tipo == "CHAR"):
        return CHAR * size + HEADER
    elif(tipo == "VARCHAR"):
        return VARCHAR * size + HEADER
    else:
        return 0

def CuantosBloques(total:int):
    return float(total / (BLOCK_SIZE - HEADER))

def Formato(number:int):
    if number >= KB and number < MB:
        return str(float(number / KB)) + " Kilobytes"
    elif number >= MB and number < GB:
        return str(float(number / MB)) + " Megabytes"
    elif number >= GB:
        return str(float(number / GB)) + " Gigabytes"
    else:
        return str(number) + " Bytes"
        
if __name__ == "__main__":
    os.system("cls")
    total = 0
    salir = 0
    print("Calcular el tamaño de cada campo.")
    while salir != 1:
        print("Agregar columna")
        tipo = input("Tipo: ")
        size = int(input("Longitud: "))
        total += CalcularColumna(tipo, size)
        salir = int(input("Continuar agregando columnas? (0=SI|1=NO) "))
    bloque = int(input("Tamaño del bloque (0=Valor por defecto: 1024 bytes): "))
    cabezera = int(input("Tamaño de la cabezera (0=Valor por defecto: 100 bytes): "))
    if(bloque != 0):
        BLOCK_SIZE = bloque
    if(cabezera != 0):
        BLOCK_HEADER = cabezera
    total += MYSQL_SIZE
    bloques = CuantosBloques(total)
    print("\n\nResultados")
    print("Tamaño del registro: {}\nCantidad total de bloques usados por registro: {}".format(Formato(total), bloques))