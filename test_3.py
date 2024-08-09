from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Erika"
    edad = 39
    estatura = 1.61
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    #assert captured.out == "nombre: Erika\nedad: 39\nestatura: 1.61\n"
