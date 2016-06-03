def nota_media(basicas, no_basicas, porcentaje_basicas, porcentaje_no_basicas):
    suma_basicas = 0
    suma_no_basicas = 0
    nota_media_basicos = 0
    nota_media_no_basicos = 0
    nota_media_basicos_porcentaje = 0
    nota_media_no_basicos_porcentaje = 0
    total_sobre_5 = 0
    total_sobre_10 = 0
    calificacion = ''
    grado = ''

    for item in basicas:
        suma_basicos = float(suma_basicos) + float(item)
    for num in no_basicas:
        suma_no_basicos = float(suma_no_basicos) + float(num)

    nota_media_basicos = suma_basicos / len(basicas)
    nota_media_no_basicos = suma_no_basicos / len(no_basicas)

    nota_media_basicos_porcentaje = nota_media_basicos * (porcentaje_basicas / 100)
    nota_media_no_basicos_porcentaje = nota_media_no_basicos * (porcentaje_no_basicas / 100)

    total_sobre_5 = nota_media_basicos_porcentaje + nota_media_no_basicos_porcentaje

    total_sobre_10 = ((total_sobre_5 - 1) * 10) / 4

    if total_sobre_10 >= 5:
        calificacion = 'aprobado'
    else:
        calificacion = 'suspenso'

    if total_sobre_10 < 5 and total_sobre_10 >= 0:
        grado = 'insuficiente'
    elif total_sobre_10 >= 5 and total_sobre_10 < 6:
        grado = 'suficiente'
    elif total_sobre_10 >= 6 and total_sobre_10 < 7:
        grado = 'bien'
    elif total_sobre_10 >= 7 and total_sobre_10 < 9:
        grado = 'notable'
    elif total_sobre_10 >= 9 and total_sobre_10 <= 10:
        grado = 'sobresaliente'
    else:
        print("Algo no ha ocurrido como sebería")

    print('Estas ', calificacion, ' con un ', grado, ' y una nota de ', total_sobre_10)


print(nota_media(notas_basicas, notas_no_basicas, porcentaje_basicos, porcentaje_no_basicos))

print('By: Alejandro Rodríguez Uson, Twitter:@alejandro99aru')


