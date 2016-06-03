print('''
Bienvenido, recuerde poner los decimales con un " . "
''')

nombre = input('''¿Cual es su nombre?''')

nota = input("¿Tu nota teórica es superior a 4?")

# Nos asegguramos de no continuar si la nota es inferior a 4
if (nota == 'NO' or nota == 'No' or nota == 'no'):

    print('No se puede calcular la media porque su calificacion teórica es menor que 4')

    nota =print('''
    Vuelva a introducir otra nota''')
else:

# Preguntamos por la nota de los examenes
    opcion_examen = int(input('¿Cuantos examenes realizados, 1 o 2?'))
    if opcion_examen == 1:
        examen_final = float(input('¿Cual es su nota en el examen?'))
        if examen_final < 0 or examen_final > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(examen_final), 'y es te es un valor que no se encuentra entre 0 y 10')
            exit(0) # con el exit cerramos el programa ya que la variable examen_final no se situa entre 0 y 10
        else:
            print('Todo perfecto, continuemos')
    else:
        examen_1= float(input('¿Cual es su nota en el primer examen?'))
        examen_2= float(input('¿Cual es su nota en el segundo examen?'))
        examen_final = round((examen_1 + examen_2) / 2, 2)
        if examen_1 < 0 or examen_1 > 10:
            print('''
                Ha habido un problema.
            ''')
            print('Parece que has introducido', str(examen_1),'en el examen 1 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        elif examen_2 < 0  or examen_2 > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(examen_2), 'en el examen 2 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        else:
            print('Todo perfecto, continuemos')


# Preguntamos por la nota de las practicas
    opcion_practica = int(input('''¿Cuantas practicas realizadas, 1 o 2?'''))
    if opcion_practica == 1:
        practica_final = float(input('¿Cual es su nota en la practica?'))
        if practica_final < 0 or practica_final > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(practica_final),'y este es un valor que no se encuentra entre 0 y 10')
            exit(0)  # con el exit cerramos el programa ya que la variable examen_final no se situa entre 0 y 10
        else:
            print('Todo perfecto, continuemos')
    else:
        practica_1 = float(input('¿Cual es su nota en la primera practica?'))
        practica_2 = float(input('¿Cual es su nota en la segunda practica?'))
        practica_final = round((practica_1 + practica_2) / 2, 2)
        if practica_1 < 0 or practica_1 > 10:
            print('''
            Ha habido un problema.
            ''')
            print('Parece que has introducido', str(practica_1), 'en la practica 1 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        elif practica_2 < 0 or practica_2 > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(practica_2), 'en la practica 2 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        else:
            print('Todo perfecto, continuemos hacia los trabajos')



# Preguntamos por las notas de los trabajos
    opcion_trabajo = int(input('¿Cuantos trabajos realizados, 1 o 2?'))
    if opcion_trabajo == 1:
        trabajo_final = float(input('¿Cual es su nota en la practica?'))
        if trabajo_final < 0 or practica_final > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(trabajo_final),
                  'y este es un valor que no se encuentra entre 0 y 10')
            exit(0)  # con el exit cerramos el programa ya que la variable examen_final no se situa entre 0 y 10
        else:
            print('Todo perfecto, continuemos hacia los trabajos')
    else:
        trabajo_1 = float(input('¿Cual es su nota en la primera practica?'))
        trabajo_2 = float(input('¿Cual es su nota en la segunda practica?'))
        trabajo_final = round((trabajo_1 + trabajo_2) / 2, 2)
        if trabajo_1 < 0 or trabajo_1 > 10:
            print('''
            Ha habido un problema.
            ''')
            print('Parece que has introducido', str(trabajo_1), 'en el trabajo 1 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        elif trabajo_2 < 0 or trabajo_2 > 10:
            print('''
                Ha habido un problema.
                ''')
            print('Parece que has introducido', str(trabajo_2), 'en el trabajo 2 y este es un valor que no se encuentra entre 0 y 10')
            exit(0)
        else:
            print('Felicidades, todo ha salido correcto')


# Obtenemos las calificaciones
    nota_examen = round(examen_final * 0.5, 2)
    nota_practica = round(practica_final * 0.3, 2)
    nota_trabajos = round(trabajo_final * 0.2, 2)

    nota_final = round(nota_examen + nota_practica + nota_trabajos, 2)


#Establecer la nota final, si es un sobre, un notable...

    if nota_final > 4 and nota_final < 5:
        print(nombre, 'tu nota es un insuficiente, ya que la media le da', nota_final)
    elif nota_final > 5 and nota_final < 6:
        print(nombre, 'tu nota es un suficiente, ya que la media le da', nota_final)
    elif nota_final > 6 and nota_final < 7:
        print(nombre, 'tu nota es un bien, ya que la media le da', nota_final)
    elif nota_final > 7 and nota_final < 9:
        print(nombre, 'tu nota es un notable, ya que la media le da', nota_final)
    elif nota_final > 9 and nota_final < 10:
        print(nombre, 'tu nota es un sobresaliente, ya que la media le da', nota_final)
    else:
        print(nombre, 'ha habido un error vuelva a ejecutar el programa, gracias.')


print('''
By: Alejandro Rodriguez Uson, 1º Bachillerato C
''')
