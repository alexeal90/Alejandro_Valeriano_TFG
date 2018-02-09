F
1.- Memoria: He creado un google doc en el google drive que se llama memoria. Aquí tengo un esquema que hice para un compañero y que voy a ir adaptando. La idea es comenzar con la parte de introducción, como ves te he puesto unas cuantas indicaciones de esta parte. Comienza a escribir por aquí. Apóyate todo lo que puedas en la memora de TFM de Beatriz, que tienes en la carpeta de referencias. En unos días te hago un listado completo de los diferentes capítulos y secciones y lo que tendrías que ir escribiendo en cada uno. Lo que te pediría es que a parte de la memoria del TFM, buscases un poco por tu cuenta, o bien en las referencias que se incluyen en la memoria de TFM. Cada vez que pongas algo que hayas sacada de una referencias, hay que ponerla como tál (hay que citarla en el texto).

2.- No hemos hablado de en qué formato vas a hacerlo. Yo prefiero LaTeX, pero no hay ningún problema en que la hagas con Word. Es más si quieres puedes ir escribiendola en el google drive y así te la puedo ir revisando más fácil y luego la vuelcas a word para tener el formato final que se pide en la normativa.

3.- Código: vamos a trabajar con una base de datos que está en Physionet. Te he creado una carpeta en google drive que se llama base de datos. Aquí viene explicado de dónde he sacado la base de datos y el artículo de referencia. Tienes que leer con cuidado, tanto lo que yo he escrito  (que te permitirá crear el código necesario para el análisis), como las referencias de Physionet de la base de datos como el artículo, esto te permitirá luego escribir la sección correspondiente de la base de datos en la memoria.
En cuanto al análisis de datos. En el github está el código para descargar la base de datos, también está descargada, y que permite visualizar un ejemplo. Corre el script database_download.py, como la base de datos ya está descargada en el github, no la vuelve a descargar, pero muestra los elementos que tiene y pinta un ejemplo de señal. Ojo, tienes que instalar un paquete de pip

pip install wfdb

que permite manejar los datos de physionet.

Con esto ya tendrías lo suficiente para poder manejar la base de datos. Por otro lado, está el script database_processing.py Este es el que vamos a utilizar para analizar cada señal de fhr. En este código se recorren los ficheros de la base de datos y para cada uno se lee la señal y la documentación de cada registro, se hace un pequeño preprocesado y luego está una parte de código que es la que tienes que completar tú. Deberás crear un dictionario con los campos que te he indicado en el documento de la base de datos, así como computar los índices, vamos a utilizar dos de sampen, uno que sea con la r = 0.15*std(fhr), y otra que sea fija y que sea r = 0.15*s, donde s es el valor medio de las desviaciones estandar para todas los fhr. Es decir, tendrás que recorrer todos los datos, calcular la std para cada uno y obtener el valor medio. Luego tendrás que calcular el valor de time irreversibility para cada uno de los fhr. Todo eso lo tienes que almacenar en el diccionario. También tendrás que almacenar información de los ficheros de cabecera, que se guarda en la variable fields, y de aquí extraer el pH y Apgar 1 y 5 para cada uno de los fetos. Cuando tengas completo el diccionario, deberás guardarlo utilizando np.save(), échale un vistazo a la documentación. Guarda como nombre del fichero el fet_id.

Esto podría tardar un poco, porque son muchas muestras (1200) y muchos datos, pero una vez que esté, ya sólo faltaría hacer un pequeño análisis estadístico de los datos.


-------o---------

DDBB
Base de datos:

Descripción de la base de datos

https://www.physionet.org/pn3/ctu-uhb-ctgdb/

.-Describe profusamente la base de datos.
.- Utiliza com referencia tanto el paper como la descripción de physionet.


Manejo base de datos con python.

Vamos a utilizar diccionarios de python, un diccionario por feto, para almacenar la información de los índices que calculemos sobre cada feto.

De esta forma cada feto tendrá:

Fet = {id:’’, sampen_r1:‘’, sampen_r2:’’; time_irrever:’’, case: ‘’, apgar_1: ‘’ ,apgar_5:’’, ph: ‘’}

Vamos a hacer, lo que tienes que hacer es un for que recorra la base de datos:

For pat in data:
	Read data
	Extract: id, apgar_1, apgar_5, ph
	Create dicc with this data
	Compute sampen_r1, sampren_r2, time_irrever
	% vamos a utilizar los 30 primeros minutos de registro para cada señal
	% Lo suyo es que capturases algunos pantallazos de señales
	Compute sd (standard deviation)
	Save those idx in the in the dicc
	Save dicc with name dict_id (where id is the corresponding id)

Con esto tendríamos todos los datos almacenados de forma que lo siguiente que tendríamos que hacer es simplemente un análisis sencillo estadístico para ver si hay alguna diferencia.

