#!/usr/bin/env python
# coding: utf-8

# # Hola Eduardo!
# 
# Mi nombre es David Bautista, soy code reviewer de Tripleten y hoy tengo el gusto de revisar tu proyecto.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - por favor, no los muevas, no los modifiques ni los borres.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div>
# 
# ¡Empecemos!

# Una empresa de comercio electrónico, Store 1, recientemente comenzó a recopilar datos sobre sus clientes. El objetivo final de Store 1 es comprender mejor el comportamiento de sus clientes y tomar decisiones basadas en datos para mejorar su experiencia online.
# 
# Como parte del equipo de análisis, tu primera tarea es evaluar la calidad de una muestra de datos recopilados y prepararla para futuros análisis.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Muy bien, recuerda que para todo los proyectos que realices es importante genera un contexto donde se comente que trata el caso y cuáles con los objetivos a cumplir, además es indispensable que se genere una tabla de contenido con el fin de mantener el orden en la entrega.
#     
# </div>

# # Cuestionario
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.

# In[1]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. El tipo de datos para `user_id` debe cambiarse de una cadena a un número entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de datos de `user_age` es incorrecto.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En su lugar, deberíamos convertir los valores de la lista a minúsculas.

# Escribe en la celda Markdown a continuación el número de las opciones que has identificado como problemas. Si has identificado varios problemas, sepáralos con comas. Por ejemplo, si crees que los números 1 y 3 son correctos, escribe 1, 3.

# **Escribe tu respuesta y explica tu argumentación:**
#  2, 3, 4
# 
# 2)user_name se le eliminan los espacios y el guion bajo para facilitar la comparación de nombres y mejorar la lectura 
# 3)user_age es un punto flotante y es mejor representar la edad como lo que es, un númeor entero
# 4)fav_categories pasar todas las categorias a minusculas ayuda a que tengan un mismo formato y facilita la comparación a futuro entre ellas

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~La 1 es cuestionable, algunas ocasiones las identificaciones de los usuarios es más conveniente guardarlas en ``string``, en últimas este hace referencia a un código y no a un número con el cual se deban hacer operaciones aritméticas.~~
#  
# </div>

# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante:</b> Entendido entonces elimino la opción 1 de la lista de respuestas <a class="tocSkip"></a>
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo. 
# </div>

# # Ejercicio 1
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name`. Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.

# In[3]:


user_name = ' mike_reed '
user_name = user_name.strip()# eliminar los espacios en la cadena original
user_name = user_name.replace('_',' ')# reemplazar el guion bajo con el espacio

print(user_name)


# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante:</b> Cometí un error al escribir la variable "user_name" y puse "username", ya lo he corregido y el resto del proyecto deberia funcionar correctamente. Saludos <a class="tocSkip"></a>
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto, continuemos con la revisión.
# </div>

# # Ejercicio 2
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[4]:


user_name = 'mike reed'
name_split = user_name.split() # divide aquí el string user_name

print(name_split)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo con el split 
# </div>

# # Ejercicio 3
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.

# In[5]:


user_age = 32.0
user_age = int(user_age)# cambia el tipo de datos para la edad de un usuario o usuaria

print(user_age)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo modificando el tipo de dato de la variable.
# </div>

# # Ejercicio 4
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[6]:


user_age = 'treinta y dos' # aquí está la variable que almacena la edad como un string.

try:
    user_age_int = int(user_age)# escribe un código que intente transformar user_age en un entero y si falla, imprime el mensaje especificado
except:
    print('Please provide your age as a numerical value.')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto.</div>

# # Ejercicio 5
# 
# Finalmente, considera que todas las categorías favoritas se almacenan en mayúsculas. Para llenar una nueva lista llamada `fav_categories_low` con las mismas categorías, pero en minúsculas, itera los valores en la lista `fav_categories`, modifícalos y agrega los nuevos valores a la lista `fav_categories_low`. Como siempre, muestra el resultado final.

# In[7]:


fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for categorie in fav_categories:
    fav_categories_low.append(categorie.lower())# escribe tu código aquí

# no elimines la siguiente declaración print
print(fav_categories_low)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Genial, buen trabajo.</div>

# # Ejercicio 6
# 
# Hemos obtenido información adicional sobre los hábitos de gasto de nuestros usuarios y usuarias, incluido el importe gastado en cada una de sus categorías favoritas. La gerencia está interesada en las siguientes métricas:
# 
# - Importe total gastado por el usuario o la usuaria.
# - Importe mínimo gastado.
# - Importe máximo gastado.
# 
# Vamos a calcular estos valores y mostrarlos en la pantalla:

# In[8]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category)# Calcula importe gastado
max_amount = max(spendings_per_category)# Importe máximo gastado
min_amount = min(spendings_per_category)# Importe mínimo gastado

# no elimines la siguiente declaración print
print(total_amount)
print(max_amount)
print(min_amount)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Bien hecho.</div>

# # Ejercicio 7
# 
# La empresa quiere ofrecer descuentos a sus clientes leales. Los clientes y las clientas que realizan compras por un importe total mayor a $1500 se consideran leales y recibirán un descuento.
# 
# Nuestro objetivo es crear un bucle `while` que compruebe el importe total gastado y se detenga al alcanzarlo. Para simular nuevas compras, la variable `new_purchase` genera un número entre 30 y 80 en cada iteración del bucle. Esto representa el importe de dinero gastado en una nueva compra y es lo que hay que sumar al total.
# 
# Una vez que se alcance el importe objetivo y se termine el bucle `while`, se mostrará la cantidad final.

# In[9]:


from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount: #condicionamos el tope en 1500 
	new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
	total_amount_spent += new_purchase # Sumamos la nueva compra al total

print(total_amount_spent)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.</div>

# # Ejercicio 8
# 
# Ahora tenemos toda la información sobre un cliente o una clienta de la forma que queremos que sea. La gerencia de una empresa nos pidió proponer una forma de resumir toda la información sobre un usuario o una usuaria. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).

# In[10]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_id = int(user_id) #convertimos el id de string a entero
user_info = f"User {user_id} is {user_name[0]} who is {user_age} years old." # escribimos la cadena formateada como nos  solicitan

# no elimines la siguiente declaración print
print(user_info)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Genial, buen trabajo.</div>

# Como sabes, las empresas recopilan y almacenan datos de una forma particular. Store 1 desea almacenar toda la información sobre sus clientes y clientas en una tabla.
# 
# | user_id | user_name | user_age | purchase_category | spending_per_category |
# | --- | --- | --- | --- | --- |
# | '32415' | 'mike', 'reed' | 32 | 'electronics', 'sport', 'books' | 894, 213, 173 |
# | '31980' | 'kate', 'morgan' | 24 | 'clothes', 'shoes' | 439, 390 |
# 
# En términos técnicos, una tabla es simplemente una lista anidada que contiene una sublista para cada usuario o usuaria.
# 
# Store 1 ha creado una tabla de este tipo para sus usuarios y usuarias. Se almacena en la variable `users`. Cada sublista contiene el ID del usuario o la usuaria, nombre y apellido, edad, categorías favoritas y el importe gastado en cada categoría.

# # Ejercicio 9
# 
# Para calcular los ingresos de la empresa, sigue estos pasos.
# 
# 1. Utiliza `for` para iterar sobre la lista `users`.
# 2. Extrae la lista de gastos de cada usuario o usuaria y suma los valores.
# 3. Actualiza el valor de los ingresos con el total de cada usuario o usuaria.
# 
# Así obtendrás los ingresos totales de la empresa que mostrarás en la pantalla al final.

# In[11]:


users = [
	  # este es el inicio de la primera sublista
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
        [894, 213, 173]
    ], # este es el final de la primera sublista

    # este es el inicio de la segunda sublista
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'shoes'],
        [439, 390]
    ] # este es el final de la segunda sublista
]

revenue = 0

for user in users:
	spendings_list = user[-1]# extrae la lista de gastos de cada usuario o usuaria y suma los valores
	total_spendings = sum(spendings_list)# suma los gastos de todas las categorías para obtener el total de un usuario o una usuaria en particular
	revenue += total_spendings# actualiza los ingresos

# no elimines la siguiente declaración print
print(revenue)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Te veo muy bien con el uso de los bucles, que bueno.</div>

# # Ejercicio 10
# 
# Recorre la lista de usuarios y usuarias que te hemos proporcionado y muestra los nombres de la clientela menor de 30 años.

# In[12]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users: #Se usa un ciclo for para recorrer el arreglo
    if user[2] < 30: #Se compara si el indice 2 es menor a 30 años
        name = user[1][0] + ' ' + user[1][1] #concatena los nombres en una variable name
        print(name)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto.</div>

# # Ejercicio 11
# 
# Juntemos las tareas 9 y 10 e imprimamos los nombres de los usuarios y las usuarias que tengan menos de 30 años y un gasto total superior a 1000 dólares.

# In[13]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]


for user in users:
    age = user[2] #guarda la edad de la lista en la variable
    total_spent = sum(user[4]) #suma el gasto total en la sublista
    name = user[1][0] + ' ' + user[1][1] #guarda en la variable name la concatenación de nombre y apellido

    if age < 30 and total_spent > 1000: #cumple las condiciones pedidas e ser menor a 30 años y tener mas de 1000 en gasto total
        print(name) #imprime el nombre
    elif age < 30:
        print(f"{name} (Gasto insuficiente)") #manda el mensaje de gasto insuficiente
    elif total_spent > 1000:
        print(f"{name} (Edad insuficiente)") # manda el mensaje de edad insuficiente


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.</div>

# # Ejercicio 12
# 
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa. Imprime el nombre y la edad en la misma declaración print.

# In[14]:


users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'],
     [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439,
     390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'],
     [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics',
     'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234,
     329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213,
     659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'],
     [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'
     ], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'],
     [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'
     ], [189, 299, 579]],
    ]

for user in users: #Se recorre la lista con el ciclo for
    if 'clothes' in user [3]: #Se averigua si la sublista contiene clothes en sus valores
        name = user[1][0] + ' ' + user[1][1] #Se concatena nombre y apellido y se mandan dentro de la variable name
        age = user[2] #se guarda la edad en la variable age
        print(f"Nombre: {name}, Edad: {age}.")#Se imprime nombre y edad. 


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Perfecto.</div>

# #Escribe aquí cualquier comentario o reflexión final

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
#     
# 
# ~~Hola Eduardo, fíjate que hay un problema con el nombre de la variable, se está intentando aplicar un método a una variable que no existe. Teniendo en cuenta el error en la sección, el resto del proyecto no se logró ejecutar exitosamente, te recomiendo revisar el error y podremos continuar con una revisión exitosa del proyecto.~~</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #2
#     
# 
# Buen trabajo Eduardo, te felicito por el desarollo de este primer proyecto.</div>
