# pg2.practica3_displinaAPI
## API de Localización de Talleres de Chapa y Pintura, Expertos en Vehículos y Proveedores de Repuestos
Esta API permite localizar, consultar y administrar información sobre talleres especializados en chapa y pintura, expertos en tipos específicos de vehículos (como clásicos, eléctricos, 4x4, etc.) Y proveedores de repuestos automotrices, facilitando la conexión entre usuarios que necesitan servicios específicos y los profesionales más adecuados cerca de su ubicación.


La API también gestiona información sobre proveedores de repuestos automotrices, permitiendo localizar distribuidores por cercanía, tipo de repuesto o marca.


## ¿Qué hace esta API?

Localiza talleres cercanos a una ubicación dada, permitiendo filtrar por especialidades y tipos de vehículo.

Permite buscar expertos en categorías específicas de vehículos, con información de experiencia, ubicación y especialidad.

Muestra detalles completos de cada taller o experto: ubicación exacta, contacto, servicios, tipos de vehículos atendidos, valoración y más.

Incluye proveedores de repuestos, permitiendo consultar disponibilidad, marcas, tipos de repuestos y ubicación de los distribuidores

Preparada para integrarse en sistemas móviles, apps web, o paneles administrativos.

## Diagrama de modelos 

![diagrama](image.png)

## Crear entorno virtual

```bash
python -m venv env
```
## Crear un archivo 
```bash
.gitignore
```
## Activar entorno virtual

```bash
# Windows
.\env\Scripts\activate

# Linux
source env/bin/activate
```
* Problemas de activacion 

    Windows PowerShel
```bash
Set-ExecutionPolicy Unrestricted
```

## Instalar dependencias

* antes crear un archivo "requirements.txt" y escribir la version.

```python
django == 5.2
django-extensions == 4.1
djangorestframework == 3.16.0
 ```

```bash
pip install -r requirements.txt 
```
# Crea el proyecto api Django

```bash
django-admin startproject apichapapintura
```

# luego iniciamos la api

```bash
python manage.py startapp localizacion
```

agregamos en la api "apichapapintura" buscamos el archivo "settings.py" y agregamos.

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    "rest_framework",
    'localizacion',
]

GRAPH_MODELS = {
    'app_labels': ['localizacion'],
```

dentro del archivo "localizacion", buscamos un archivo "models.py" y ponemos las entidades de nuestra Api, atributos y relaciones

# Ejemplo del archivo models
```python

class Localizacionuser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    localizaciones = models.ManyToManyField(Localizacionuser) 

class Experto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    talleres = models.ManyToManyField(Taller) 

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    talleres = models.ManyToManyField(Taller) 
    repuestos = models.ManyToManyField('Repuesto') 

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    proveedores = models.ManyToManyField(proveedor) 

```


luego instalar algunas dependencias para que pueda graficar el diagrama 

# Instalar dependencias
```bash
pip install django == 5.2
pip install django-extensions == 4.1
pip install djangorestframework == 3.16.0
pip install pydotplus
pip install django_extensions 
pip install graphviz

```

## Ejecutar el comando para el grafico
```bash
python manage.py graph_models ruta -o diagrama.png
```
![deagrama](image.png)

## Referencia de Endpoints Públicos

* Todos los servicios de la API están disponibles públicamente. Se accede a ellos mediante el prefijo /api/, y no se requiere autenticación  para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)

```bash
Localización	/api/localizaciones/     GET, POST	    Listar o registrar ubicaciones de usuarios
Taller	        /api/talleres/	         GET, POST	    Listar o registrar talleres automotrices
Taller	        /api/talleres/<id>/	     GET, PUT, DELETE	Consultar, actualizar o eliminar un taller específico
Experto	        /api/experto/	         GET, POST	    Listar o registrar expertos en tipos de vehículos
Experto     	/api/experto/<id>/	     GET, PUT, DELETE	Consultar, actualizar o eliminar un experto específico
Proveedor   	/api/proveedor/	         GET, POST	    Listar o registrar proveedores de repuestos automotrices
Proveedor	    /api/proveedor/<id>/	 GET, PUT, DELETE	Consultar, actualizar o eliminar un proveedor específico
Repuesto	    /api/repuesto/	         GET, POST	    Listar o registrar repuestos automotrices
Repuesto	    /api/repuesto/<id>/	     GET, PUT, DELETE	Consultar, actualizar o eliminar un repuesto específico
```

## 1. Localización de Usuarios (/api/localizacionusers/)
Ubicación geográfica de usuarios que buscan servicios.
```bash
GET /api/localizacionusers/
```
Descripción: Lista todas las localizaciones de usuarios.
Ejemplo:
```bash
json
Copiar
Editar
[
  {"id": 1, "nombre": "Carlos", "latitud": -34.6037, "longitud": -58.3816}
]
POST /api/localizacionusers/

Body:

json
Copiar
Editar
{"nombre": "Ana", "latitud": -33.4489, "longitud": -70.6693}
GET /api/localizacionusers/{id}/, PUT, PATCH, DELETE funcionan igual que en otros endpoints.
```
![localizacionusers](/imagenes/API-localizacion.png)
## 2. Talleres (/api/talleres/)
Talleres de chapa y pintura registrados.
```bash
GET /api/talleres/
```
Descripción: Lista todos los talleres.

Ejemplo:
```bash
json
Copiar
Editar
[
  {
    "id": 1,
    "nombre": "Taller Don Pepe",
    "direccion": "Av. Siempre Viva 742",
    "telefono": "123456789",
    "email": "donpepe@taller.com",
    "latitud": -34.60,
    "longitud": -58.38,
    "localizaciones": [1]
  }
]
POST /api/talleres/

Body:

json
Copiar
Editar
{
  "nombre": "Taller Rápido",
  "direccion": "Calle 123",
  "telefono": "0987654321",
  "email": "rapido@taller.com",
  "latitud": -34.61,
  "longitud": -58.37,
  "localizaciones": [1, 2]
}
```
![talleres](/imagenes/API-taller.png)
## 3. Expertos (/api/expertos/)
Profesionales que trabajan con talleres.
```bash
GET /api/expertos/
```
Ejemplo:
```bash
json
Copiar
Editar
[
  {
    "id": 1,
    "nombre": "Luis Gómez",
    "direccion": "Calle Expertos 456",
    "telefono": "1122334455",
    "email": "luis@experto.com",
    "latitud": -34.62,
    "longitud": -58.36,
    "talleres": [1]
  }
]
POST /api/expertos/

Body:

json
Copiar
Editar
{
  "nombre": "Laura Díaz",
  "direccion": "Av. del Trabajo 789",
  "telefono": "3344556677",
  "email": "laura@experta.com",
  "latitud": -34.63,
  "longitud": -58.35,
  "talleres": [1, 2]
}
```
![expertos](/imagenes/API-experto.png)
## 4. Proveedores (/api/proveedors/)
Proveedores de piezas para talleres.
```bash
GET /api/proveedors/
```
Ejemplo:
```bash
json
Copiar
Editar
[
  {
    "id": 1,
    "nombre": "Autopartes SRL",
    "direccion": "Ruta 40 Km 10",
    "telefono": "456789123",
    "email": "contacto@autopartes.com",
    "latitud": -34.64,
    "longitud": -58.34,
    "talleres": [1],
    "repuestos": [1]
  }
]
POST /api/proveedors/

Body:

json
Copiar
Editar
{
  "nombre": "Distribuidora Nacional",
  "direccion": "Av. Piezas 202",
  "telefono": "321654987",
  "email": "ventas@dnacional.com",
  "latitud": -34.65,
  "longitud": -58.33,
  "talleres": [1],
  "repuestos": [1, 2]
}
```
![proveedores](/imagenes/API-proveedor.png)
## 5. Repuestos (/api/repuestos/)
Piezas y componentes utilizados en los servicios.
```bash
GET /api/repuestos/
```
Ejemplo:
```bash
json
Copiar
Editar
[
  {
    "id": 1,
    "nombre": "Paragolpes delantero",
    "direccion": "Depósito Central",
    "telefono": "123123123",
    "email": "repuestos@fabrica.com",
    "latitud": -34.66,
    "longitud": -58.32,
    "proveedores": [1]
  }
]
POST /api/repuestos/

Body:

json
Copiar
Editar
{
  "nombre": "Espejo lateral",
  "direccion": "Depósito Sur",
  "telefono": "987987987",
  "email": "stock@repuestossur.com",
  "latitud": -34.67,
  "longitud": -58.31,
  "proveedores": [1, 2]
}
```
![repuesto](/imagenes/API-repuesto.png)
## CASO DE USO: Asociar un Taller con un Usuario, un Experto y un Proveedor de Repuestos
Objetivo
Simular el flujo de creación y asociación de datos entre un usuario, un taller cercano, un experto en ese taller y un proveedor de repuestos con stock para ese taller.
```bash
Flujo Paso a Paso:
1. Crear una Localización de Usuario
POST /api/localizacionusers/

json
Copiar
Editar
{
  "nombre": "Usuario Cliente",
  "latitud": -34.6037,
  "longitud": -58.3816
}
```
```bash
2. Crear un Taller
POST /api/talleres/

json
Copiar
Editar
{
  "nombre": "Taller Solución Rápida",
  "direccion": "Calle Rápida 100",
  "telefono": "111222333",
  "email": "solucion@taller.com",
  "latitud": -34.6040,
  "longitud": -58.3820,
  "localizaciones": [1]
}
```
```bash
3. Registrar un Experto Asociado al Taller
POST /api/expertos/

json
Copiar
Editar
{
  "nombre": "Miguel Técnico",
  "direccion": "Av. Técnica 999",
  "telefono": "444555666",
  "email": "miguel@experto.com",
  "latitud": -34.6030,
  "longitud": -58.3830,
  "talleres": [1]
}
```
```bash
4. Crear un Repuesto
POST /api/repuestos/

json
Copiar
Editar
{
  "nombre": "Capó frontal",
  "direccion": "Galpón Norte",
  "telefono": "555444333",
  "email": "ventas@repuestos.com",
  "latitud": -34.6050,
  "longitud": -58.3840
}
```
```bash
5. Registrar un Proveedor que ofrece ese Repuesto al Taller
POST /api/proveedors/

json
Copiar
Editar
{
  "nombre": "Suministros Express",
  "direccion": "Ruta 7 Km 15",
  "telefono": "999888777",
  "email": "express@proveedores.com",
  "latitud": -34.6060,
  "longitud": -58.3850,
  "talleres": [1],
  "repuestos": [1]
}
```
## Una aplicación cliente podría usar GET con filtros como:

/api/talleres/?localizaciones=1 → Talleres cercanos al usuario

/api/expertos/?talleres=1 → Expertos que trabajan en el taller

/api/proveedors/?talleres=1 → Proveedores que surten a ese taller

/api/repuestos/?proveedores=1 → Ver qué repuestos tiene disponible cada proveedor

* Esta API permite a las aplicaciones externas no solo cargar la información de talleres de chapa y pintura, expertos en vehículos y proveedores de repuestos utilizando los endpoints POST, sino también realizar búsquedas y filtrados avanzados mediante los endpoints GET. Esto habilita la creación de herramientas complejas, como un buscador de talleres por ubicación o un sistema para encontrar repuestos específicos para un modelo de vehículo.









