print('''
Bienvenido
''')

pregunta = input('''¿Que calculo quieres realizar?(velocidad,espacio o tiempo)''')


while not (pregunta == 'espacio' or pregunta== 'Espacio' or pregunta == 'tiempo' or pregunta== 'Tiempo' or pregunta== 'Velocidad' or pregunta =='velocidad'):

    print(
        pregunta, '''no está establecida por favor introduce espacio, tiempo o velocidad
    ''')

    pregunta = input("¿Que calculo quieres realizar?(velocidad,espacio o tiempo)")

if (pregunta== "velocidad" or pregunta== "Velocidad"):

        print('''Necesitaremos el espacio y el tiempo
        ''')

        espacio = int(input("¿Espacio en m?"))
        tiempo = int(input("¿Tiempo en s?"))

        print('''
        La velocidad es de''', round(espacio/tiempo, 2), '''m/s aproximadamente.
        ''')

elif (pregunta == "espacio" or pregunta == "Espacio"):

        print('''Necesitaremos la velocidad y el tiempo
        ''')

        velocidad = float(input("¿Velocidad m/s?"))
        tiempo = float(input("¿Tiempo s?"))

        print('''
        El espacio es de''', round(velocidad * tiempo, 2), '''m aproximadamente.
        ''')

elif (pregunta == "tiempo" or pregunta == "Tiempo"):

        print('''Necesitaremos el espacio y la velocidad
        ''')

        espacio = int(input("¿Espacio en s?"))
        velocidad = int(input("¿Velocidad m/s?"))

        print('''
        La velocidad es de''', round(espacio / velocidad, 2), '''s aproximadamente.
        ''')


print('''
Alejandro Rodríguez Usón''')
    


