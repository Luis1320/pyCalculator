# calculadora con una sola variable

print("************************************")
print("*Calculadora con una sola variable.*")
print("************************************\n")

print("Presiona 1 para sumar.")
print("Presiona 2 para restar.")
print("Presiona 3 para dividir.")
print("Presiona 4 para multiplicar.")
print("Presiona 5 para modulo o resto.")
print("Presina 6 para exponenciar.\n")

opcion = int(input("Que opcion deseas elegir:"))


if opcion == 1:
    n1 = int(input("Primer numero para sumar:"))
    n1 += int(input("Segundo numero para sumar:"))
    print(n1)

elif opcion == 2:
    n1 = int(input("Primer numero para restar:"))
    n1 -= int(input("Segundo numero para restar:"))
    print(n1)

elif opcion == 3:
    n1 = int(input("Que cantidad deseas dividir:"))
    n1 /= int(input("Dentro de cuanto deseas dividir:"))
    print(round(n1,2))

elif opcion == 4:
    n1 = int(input("Primer numero para multiplicar:"))
    n1 *= int(input("Segundo numero para multiplicar:"))
    print(n1)

elif opcion == 5:
    n1 = int(input("De que numero quieres el modulo o resto:"))
    n1 %= int(input("En cuantas partes deseas dividir el modulo:"))
    print(n1)

elif opcion == 6:
    n1 = int(input("Que numero deseas exponenciar:"))
    n1 **= int(input("Por cuanto deseas exponenciar este numero:"))
    print(n1)

else:
    print("La opcion que elegiste no existe.")
