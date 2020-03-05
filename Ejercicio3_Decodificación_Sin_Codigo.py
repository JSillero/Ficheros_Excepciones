'''
¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves... ¡impleméntala!
Reconocer algunos preposiciones y articulos, que son palabras muy comunes ," de " " a " , " y " etc;  usando contain nos daría posibles resultados correctos,
  en el caso que más de uno coincidiese se motrarían la primera linea de cada posibilidad y se dejaría que el usuario eligiese la que fuese más correcta.
  '''
import sys

'''Metodo que comprueba si la cadena pasa contiene alguna preposicion o el articulo LA o EL'''
def plausible(cadena):
    if(cadena.__contains__(" A ") or cadena.__contains__(" ANTE") or cadena.__contains__("BAJO ") or
            cadena.__contains__(" CABE ") or cadena.__contains__(" CON") or cadena.__contains__(" DE ") or
            cadena.__contains__(" DESDE ") or cadena.__contains__(" EN ") or cadena.__contains__(" ENTRE ") or
            cadena.__contains__(" HACIA ") or cadena.__contains__(" HASTA ") or cadena.__contains__(" PARA ") or
            cadena.__contains__(" POR ") or cadena.__contains__(" SEGÚN ") or cadena.__contains__(" SIN ") or
            cadena.__contains__(" SOBRE ") or cadena.__contains__(" EL ") or cadena.__contains__(" LA ") ):
        return True
    else:
        return False

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

cadena_plausible=[]

letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

'''Se prueban todas las instancias del codigo cesar'''
for y in range(1,10):
    code = y

    encoded_let = letters[code:] + letters[:code]
    letter_dic = {}

    count = 0
    for x in letters:
        letter_dic[encoded_let[count]] = x
        count += 1

    cadena="a"
    cadenacod = ""


    while(cadena != ""):
        cadena = fichero_li.readline().upper()

        for x in  cadena[:len(cadena)-1]:
            try:
                cadenacod += letter_dic[x]
            except:
                cadenacod += x
        cadenacod += "\n"
    print(cadenacod)
    '''las instancias plausibles(contienen una preposicion son almacenadas en un array'''
    if(plausible(cadenacod)):
        cadena_plausible.append(cadenacod)
    fichero_li.seek(0,0)

if(len(cadena_plausible)==0):
    print("No hay ninguna traduccion que sea posiblemente correcta.")
    exit(4)
elif(len(cadena_plausible)==1):
    print("Cadena encontrada")

    if (len(sys.argv) == 3):
        fichero_es.write(cadena_plausible[0])
    else:
        fichero_li.close()
        fichero_li = open(sys.argv[1], "w")
        fichero_li.write(cadena_plausible[0])
        fichero_li.close()
        fichero_li.close()
        exit(0)

    fichero_li.close()
    fichero_es.close()
    exit(0)
else:
    '''Muestran todas la parte inicial de las combinaciones posibles.'''
    cont=0
    print("Introduzca el numero de la cadena que sea más parecida al español normal.")
    for x in cadena_plausible:
        cont+=1
        try:
            print(cont+". "+x[:10])
        except:
            print(x[:len(x)//2])

    respuesta= int(input())

    if(len(sys.argv) == 3):
        fichero_es.write(cadena_plausible[respuesta])
    else:
        fichero_li.close()
        fichero_li = open(sys.argv[1],"w")
        fichero_li.write(cadena_plausible[respuesta])
        fichero_li.close()
        fichero_li.close()
        exit(0)


    fichero_li.close()
    fichero_es.close()

