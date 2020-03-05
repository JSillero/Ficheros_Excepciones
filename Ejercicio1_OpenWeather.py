'''1. Usando esta API de OpenWeather que nos da el pronóstico del
tiempo para una ciudad que se le pide al usuario de los siguientes
 cinco días, mostrar:
Temperatura media, mínima y máxima (en grados Celsius) para cada
 día y global.
Temperatura media, mínima y máxima para cada día y global.
Tened en cuenta que las respuestas de esta api referentes
a los días y horas usan el tiempo en formato UNIX (UTC).

Modifica el ejercicio 1 del tema anterior de manera que:

El programa admita dos parámetros:
El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la ciudad
es errónea el programa termina con un mensaje de error y código 2.
El segundo es opcional, y si existe es el directorio donde vamos a crear un fichero html
 con la información formateada como una tabla del pronóstico de la temperatura, si no existe
  la información se muestra por pantalla. Consideraciones:
este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo:
 "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html"
si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje
de error (código 1) diciendo que la sintaxis es incorrecta.
Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando
 qué hace.


@author: Jose Sillero
'''
import null
import requests
import sys
import os


if(len(sys.argv)< 1  or len(sys.argv)>3 ):
    print("La sintaxis es incorrecta")
    exit(1)

if(sys.argv[1]=="-h"):
    print("Este programa devuelve la temperatura minima maxima y media de los proximos cinco dias en la ciudad pasada por el primer parametro. \n"
          "El segundo parametro es opcional y denota la direccion del fichero html en el que se creará una tabla con la informacion proporcionada.")
    exit(0)

ciudad=sys.argv[1]
try:
    fichero=sys.argv[2]
except:
    fichero=null

apikey= os.environ['WeatherApi']
url="https://api.openweathermap.org/data/2.5/forecast"
parametros = {'q':ciudad,'mode':'json','units':'metric','APPID':'3ad17004b56c3977e6536ac7a6ee46e3','cnt': '50'}


r=requests.get(url,params=parametros)

'''
para comprobar datos descomentar
print(r.url)
print(r.headers)
'''
datos=r.json()

'''
para comprobar datos descomentar
print(datos)
'''

if datos['cod'] == '404':
    print("La ciudad no existe")
    exit(2)

'''se coge la primera fecha y se le suman 24 horas en segundos para que la siguiente que se muestre sea dentro de 1 dia'''
fecha_sec=datos['list'][0]["dt"]+86400

'''Coge la fecha en la que se saca la temperatura y quita la hora'''
fecha=datos['list'][0]["dt_txt"][0:10]

if fichero is null:
    print("Temperatura media hoy ",fecha," en ", ciudad ,": ", datos['list'][0]["main"]["temp"])
    print("Temperatura maxima hoy ",fecha ," en ", ciudad ,": ", datos['list'][0]["main"]["temp_max"])
    print("Temperatura minima hoy ",fecha," en", ciudad ,": ", datos['list'][0]["main"]["temp_min"])
    print()

    medmed = datos['list'][0]["main"]["temp"]
    medmin = datos['list'][0]["main"]["temp_max"]
    medmax = datos['list'][0]["main"]["temp_min"]
    cantidad=0

    cnt=1
    '''repite hasta que se muestren las temperaturas 4 veces más'''
    while(cantidad<4):
        '''restringe el mostrar las temperaturas a no ser que el dt sea mayor que el anterior por más de 86400(24 horas en segundos'''
        if(datos['list'][cnt]["dt"]>fecha_sec):
            cantidad+=1
            fecha_sec+=+86400
            fecha=datos['list'][cnt]["dt_txt"][0:10]
            print(cnt)
            print("Temperatura media a",fecha," en ", ciudad ,": ", datos['list'][cnt]["main"]["temp"])
            print("Temperatura maxima a",fecha ," en ", ciudad ,": ", datos['list'][cnt]["main"]["temp_max"])
            print("Temperatura minima a",fecha," en", ciudad ,": ", datos['list'][cnt]["main"]["temp_min"])
            print()

            medmed += datos['list'][cnt]["main"]["temp"]
            medmin += datos['list'][cnt]["main"]["temp_max"]
            medmax += datos['list'][cnt]["main"]["temp_min"]

        cnt+=1

    print("Temperatura media en los 5 didas en ", ciudad, ": ",  medmed/5)
    print("Temperatura maxima media en los 5 dias en ", ciudad, ": ", medmax/5)
    print("Temperatura minima media en los 5 dias en", ciudad, ": ",medmin/5)
else:
   ''' {CIUDAD}
    _
    {FECHA - INICIO}
    _
    {FECHA_FIN'''
   fichero+="/"
try:
    html=open(fichero+ciudad+datos['list'][0]["dt_txt"][0:10]+datos['list'][39]["dt_txt"][0:10]+'.html','w+')
except:
    print("La direccion especificada no existe")
    exit(3)

cadena="<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable {\n  font-family: arial, sans-serif;\n  border-collapse: collapse;\n  width: 100%;\n}\ntd, th {\n  border: 1px solid #dddddd;\n  text-align: left;\n  padding: 8px;\n}\ntr:nth-child(even) {\n  background-color: #dddddd;\n}\n</style>\n</head>\n<body>\n<table>\n  <tr>\n    <th></th>\n    <th>Media</th>\n    <th>Maxima</th>\n    <th>Minima</th>\n  </tr>\n"

cnt=0
cantidad=0
fecha_sec -= 86400

while(cantidad<5):

    if (datos['list'][cnt]["dt"] >= (fecha_sec)):
        fecha = datos['list'][cnt]["dt_txt"][0:10]
        cantidad += 1
        fecha_sec += +86400
        cadena+="<tr>\n    <td>"+fecha+"</td>\n    <td>"+str(datos['list'][cnt]["main"]["temp"])+"</td>\n    <td>"+ str(datos['list'][cnt]["main"]["temp_max"])+"</td>\n    <td>"+ str(datos['list'][cnt]["main"]["temp_min"])+"</td>\n  </tr>\n"


    cnt += 1

cadena+="</table>\n</body>"
html.write(cadena)