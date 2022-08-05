# codigos de errores unicos
# codigo           error
#  1       valor ingresado no es numero entero
#  2       parametro operacion fuera de rango
#  3        Division por cero
#  4       valor ingresado no es un string
#  5       parametro opciones fuera de rango

def basic_operations(Operando1, Operando2, Operacion):

    resultado = int

    try:
        if int(Operacion) == 1:
            resultado = int(Operando1) + int(Operando2)

        elif int(Operacion) == 2:
            resultado = int(Operando1) - int(Operando2)

        elif int(Operacion) == 3:
            if int(Operando2) == 0:
                print("ERROR 3")
            else:
                resultado = int(Operando1) / int(Operando2)
        else:
            print("ERROR 2")
    except int(Operacion):
        print("Error 1")
    return (resultado)


def count_char(oracion):
    contador = 0
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in str(oracion):
        if i in numeros:
            print("ERROR 4")

        else:
            contador = contador + 1
    return (contador)
