'''2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también pasamos como parámetro, de manera que:

Si el programa no recibe dos parámetros termina con un error 1.
Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.'''
'''JAJA SOY YO, INTERNETO EL SALUDO CONCAVO DE TU newfag.puede ha
ber mas de una linea
luego
a correr
es lo que toca lmao
'''

import os
import sys

try:
    assert len(sys.argv) == 2 or len(sys.argv) == 3

except:

    print("Numero de parametros incorrecto.")
    exit(1)

try:
    fichero_li = open(sys.argv[1],"r")
    if(len(sys.argv) == 3):
        fichero_es = open(sys.argv[2],"w")
except:
    print("Alguno de los ficheors no existe")
    exit(2)

code = int(input("Introduzca el valor de la codificación."))
letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
encoded_let = letters[code:] + letters[:code]
letter_dic = {}

count = 0
for x in letters:
    letter_dic[x]=encoded_let[count]
    count += 1

cadena = "a"
cadenacod = ""

while(cadena != ""):
    cadena = fichero_li.readline().upper()
    for x in  cadena[:len(cadena)-1]:
        try:
            cadenacod += letter_dic[x]
        except:
            cadenacod += x
    cadenacod += "\n"

if(len(sys.argv) == 3):
    fichero_es.write(cadenacod)
else:
    fichero_li.close()
    fichero_li = open(sys.argv[1],"w")
    fichero_li.write(cadenacod)
    fichero_li.close()
    fichero_li.close()
    exit(0)



fichero_li.close()
fichero_es.close()
