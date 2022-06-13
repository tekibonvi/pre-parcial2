def max_de_tres(nr1, nr2, nr3):
    if nr1 > nr2:
        if nr1 > nr3:
            return f"el mayor es {nr1}"
        else:
            return f"el mayor es {nr3}"
    else:
        if nr2 > nr3:
            return f"el mayor es {nr2}"
        else:
            return f"el mayor es {nr3}"


print(max_de_tres(1,2,3))
print(max_de_tres(5,2,3))
print(max_de_tres(1,10,3))
print(max_de_tres(2,2,2))