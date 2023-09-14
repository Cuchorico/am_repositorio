1. #Hacer un programa que imprima los números del 1 al 100, en phyton sería:

for x in range(100):
  print(x+1)


2. #Hacer un pragama que imprima los números del 1 al 100 que sean divisibles entre 3 (con resto 0)

for x in range(100):
  if((x+1) % 3 == 0):
    print(x+1)


3. #Realiza el algoritmo para un sumador de dos números. Si el resultado es menor a 100 se mostrará el mensaje "menor a 100", si el resultado es mayor a 100, pero menor a 150 mostrará el mensaje "mayor a 100", y si el resultado es mayor a 150, mostrar el mensaje "mayor a 150".

numero_1 = int(input("Ingresa un numero"))
numero_2 = 5
suma = numero_1 + numero_2
resultado = ""

if(suma<100):
  resultado = "menor a 100"
elif(suma>=100 and suma<150):
  resultado = "mayor a 100"
elif(suma>=150):
  resultado = "mayor a 150"

print(resultado)


4. 