def es_vocal(caracter):
    caracter = caracter.upper()

    if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        return True
    else:
        return False



car = input ("ingrese una letra:")


if es_vocal(car):
    print ("Es vocal")
else:
    print("No es vocal")


        