precio = float(input("¿Cúanto cuesta el producto?"))

iva = int(input("¿Cual es el IVA 4,7 ó 21?"))

if iva == 4 or iva == 7 or iva == 21:

    precio_final = precio + precio*(iva/100)

    print("Su producto tiene un precio de ", precio_final, "€,", "IVA incluido de ", iva, "%")

else:

    print("IVA incorrecto")


print("By: Alejandro Rodríguez Usón")
