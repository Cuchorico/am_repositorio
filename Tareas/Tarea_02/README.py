1. #Hacer un programa que imprima los números del 1 al 100, en phyton sería:

for x in range(100):
  print(x+1)

EXPLICACIÓN: For x in range define una función para una cifra cualquiera dentro del rango 0 a 100, print(x+1) hace que la ejecución ocurra dentro del rango 1 a 100.


2. #Hacer un programa que imprima los números del 1 al 100 que sean divisibles entre 3 (con resto 0)

for x in range(100):
  if((x+1) % 3 == 0):
    print(x+1)

EXPLICACIÓN: For x en el rango de 100 define una función para los números de 0 a 100, if condiciona esa función para que el rango comience desde 1 (x+1) y solo se impriman los números divisibles por tres (%3 == 0), print imprimirá los números bajo esta condición dentro de ese rango.

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

EXPLICACIÓN: numero_1 es la primera variable a ingresar, que corresponde a un tipo de dato de ingreso de información (input), en este caso, tu edad, la cual solo podrá corresponder a números naturales (int). Numero_2 la segunda variable la cual solo puede adquirir el valor de 5. Suma corresponde a la variable definida por la operación de suma de las anteriores, y, resultado es la suma realizada de numero_1 y numero_2 textualmente ("").
             Pero, el resultado esta condicionado con que dependiendo de su naturaleza (suma<100, suma>=100 y suma<150) ofrezca distintas respuestas respectivas (resultado = "")

4. #Generar un programa que combine variables, tipos de datos y una condicional en Python (hacer una función que evalúe si el usuario es mayor de edad y si le gusta la programación, que envíe diferentes textos según la respuesta del usuario)

edad = int(input("Ingresa tu edad"))
gusta_programar = str(input("¿Te gusta programar? (si/no)"))
resultado= ""

if (edad >= 18 and gusta_programar == "si"):
  resultado = "Eres mayor de edad y te gusta programar"
elif(edad>=18 and gusta_programar == "no"):
  resultado = "Eres mayor edad y no te gusta programar"
elif(edad<18 and gusta_programar == "no"):
  resultado = "No eres mayor de edad y no te gusta programar"
elif(edad<18 and gusta_programar == "si"):
  resultado = "No eres mayor de edad y te gusta programar"
else:
  resultado = "Ingresaste un dato erróneamente"

print(resultado)

EXPLICACIÓN: la variable edad es una de ingreso de datos [input(su edad)] y siendo esta solo  números naturales (int), por su parte, la variable gusta_programar también es de ingreso de información, pero escrita (str) y binaria (si/no). La variable resultado presentará una conclusión textual ("") la cual tendrá 4 casos a los que estará condicionada que combinan la variable edad y gusta_programar, se añade un quinto en caso de que haya un ingreso de datos erróneo o ajeno a las indicaciones. El print imprimirá el resultado.