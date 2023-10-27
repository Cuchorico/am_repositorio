# Data Self Portrait

La historia que pretendo contar a través de mi visualización atómica es cuál es día de la semana en que suelo caminar más en base a la acumulación de pasos categorizada por día de la semana durante los 31 en que se efectuó la medición.

El resultado final arrojó que, según la cantidad de pasos fusionada de todos los miércoles transcurridos durante la medición (31 días), este correspondería al día en que más caminatas efectúo al mes. Ello encontraría explicación en que es la única jornada durante el semestre en que me quedo a almorzar en la universidad, teniendo que recorrer facultades buscando un microondas para calentar mi comida o esperar parado a que termine de calentarse en el aparato.


# Pasos del procedimiento:

1) Para empezar a contar este aspecto sobre mí, tuve que volver a la base de datos inicial y modificarla, añadiendo una columna sobre el día de la semana en que los pasos fueron efectuados.


2) Luego, decidí graficar con la libreria de Pandas, ya que se me hacía más sencilla de manipular en código y consideré que era justo el tipo de graficación que los datos de mi historia requerían. Por tanto, me dirigí a la biblioteca disponible en nuestro GitHub (pandas_altair_vis.ipynb) y copié el código para importar mi base de datos. Le hice algunas modificaciones al código, como la variable que le quería otorgar a el dataframe, su dirección de enlace y el nombre con que fue subida a Coolab.

import pandas as pd 
nRowsRead = None
Pasos_1 = pd.read_csv('/content/drive/MyDrive/Tarea_04.csv', delimiter=';', nrows = nRowsRead, encoding="latin-1")
Pasos_1.dataframeName = 'Tarea_04.csv'
nRow, nCol = Pasos_1.shape
print(f'There are {nRow} rows and {nCol} columns') 


3) A continuación, agrupé la columna "Pasos x Día" en base a la de "Día de la semana", utilizando la función .sum() para combinar las variables que se repitieran de la columna "Día de la semana"  en una sola celda, y, por tanto, sus pares en la columna "Pasos x Día" también lo harían (si pasos en distintas celdas se efectuaron ambos un lunes, la cantidad de pasos se sumaba en una sola fila indicando un solo día).

Pasos_1_dia = Pasos_1.groupby("Día de la semana")["Pasos x Día"].sum()
Pasos_1_dia 


4) Tras esto, tuve que generar un nuevo dataframe desde cero, ya que en el creado anteriormente, los días de la semana quedaban desordenados cronológicamente.

import pandas as pd

ordenado = [["Lunes", 6507],
          ["Martes", 17400],
          ["Miércoles", 51492],
          ["Jueves", 19421],
          ["Viernes", 31666],
          ["Sábado", 14264],
          ["Domingo", 11931]]

df = pd.DataFrame(ordenado, columns= ["Día", "Pasos Acumulados (31 días)"])

print(df)


5) Finalmente, y copiando de nuevo un código de la biblioteca "pandas_altair_vis.ipynb", grafiqué los datos, pero no sin antes hacerle unas modificaciones la código original, como el tener que indicar y recalcar el nombre de los ejes y a qué columna debía graficar cada uno, porque, en primera instancia, el eje X reemplazaba la variable "Día" de la semana por números.

ax = df.plot(kind="bar", fontsize=8, x= "Día", y= "Pasos Acumulados (31 días)")
ax.set_xlabel("Día")
ax.set_ylabel("Pasos Acumulados (31 días)")
ax.set_title(None)
ax 