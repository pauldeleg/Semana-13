# Restaurante App
## Jonnathan Paul Deleg Condo

Aplicación desarrollada en Python para la asignatura **Programación Orientada a Objetos**.

En la Semana 13 se inicia la transición de la aplicación basada en consola hacia una aplicación con **interfaz gráfica de usuario (GUI)** utilizando **Tkinter**.

El proyecto mantiene la separación entre modelos, servicios, archivos de datos e interfaz gráfica, siguiendo la estructura trabajada durante las semanas anteriores.

## Objetivo

Implementar una estructura gráfica inicial para `restaurante_app`, integrando los modelos `Producto` y `Usuario` con archivos JSON y una interfaz desarrollada mediante Tkinter.

La aplicación permite realizar una simulación de acceso mediante usuario y contraseña y, después de un ingreso correcto, consultar los productos y usuarios registrados.

## Tecnologías utilizadas

* Python
* Tkinter
* Programación Orientada a Objetos
* Archivos JSON
* Git y GitHub

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
```

## Descripción de las carpetas

### `datos/`

Contiene los archivos JSON utilizados para almacenar información local de la aplicación.

* `productos.json`: almacena los productos registrados del restaurante.
* `usuarios.json`: almacena los usuarios y las credenciales utilizadas para la simulación de acceso.

### `modelos/`

Contiene las clases principales del sistema.

#### `producto.py`

Define la clase `Producto`, encargada de representar los productos del restaurante.

El modelo mantiene propiedades, setters y validaciones para controlar los datos de los productos.

#### `usuario.py`

Define la clase `Usuario`, encargada de representar a los usuarios del sistema.

También utiliza propiedades, setters y validaciones para controlar la información de los usuarios y sus credenciales.

### `servicios/`

Contiene la lógica que permite trabajar con los datos de la aplicación.

#### `archivo_servicio.py`

Se encarga de realizar la lectura de los archivos JSON.

Su responsabilidad es trabajar con los archivos de datos sin mezclar esta tarea con la interfaz gráfica.

#### `restaurante_servicio.py`

Centraliza las operaciones relacionadas con los usuarios y productos.

Entre sus responsabilidades se encuentran:

* Convertir los datos cargados en objetos.
* Validar el usuario y la contraseña.
* Listar los usuarios registrados.
* Listar los productos registrados.
* Consultar las cantidades de usuarios y productos.

### `ui/`

Contiene las vistas de la interfaz gráfica desarrolladas con Tkinter.

#### `login_view.py`

Presenta la pantalla inicial de acceso.

Permite ingresar:

* Usuario.
* Contraseña.

También muestra mensajes cuando los campos están vacíos o las credenciales son incorrectas.

#### `main_view.py`

Presenta la interfaz principal después de un ingreso correcto.

Permite consultar:

* Productos registrados.
* Usuarios registrados.
* Ventas, identificada como una funcionalidad pendiente para una etapa posterior.

También permite cerrar sesión y regresar a la pantalla de acceso.

## `main.py`

Es el punto de entrada de la aplicación.

Sus principales responsabilidades son:

1. Crear la ventana principal de Tkinter.
2. Preparar los servicios.
3. Cargar la información de los archivos JSON.
4. Crear `RestauranteServicio`.
5. Mostrar inicialmente `LoginView`.
6. Cambiar entre `LoginView` y `MainView`.
7. Mantener una única ventana principal y un único ciclo de ejecución de Tkinter.

## Flujo de funcionamiento

```text
Inicio de la aplicación
          ↓
       main.py
          ↓
Carga de productos y usuarios
          ↓
RestauranteServicio
          ↓
      LoginView
          ↓
Usuario y contraseña
          ↓
Validación de acceso
       ↙       ↘
 Incorrecto    Correcto
     ↓             ↓
  Mensaje       MainView
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
    Productos   Usuarios   Ventas
                              ↓
                          Pendiente
                   ↓
              Cerrar sesión
                   ↓
               LoginView
```

## Inicio de sesión

Para realizar las pruebas de funcionamiento se deben utilizar las credenciales registradas en `datos/usuarios.json`.

Por ejemplo:

```text
Usuario: admin
Contraseña: 1234
```

Estas credenciales son únicamente para la simulación de acceso de la aplicación.

## Funcionamiento de los productos

Los productos se encuentran almacenados en `datos/productos.json`.

La interfaz gráfica no accede directamente al archivo JSON para mostrar los productos.

El flujo utilizado es:

```text
productos.json
      ↓
ArchivoServicio
      ↓
RestauranteServicio
      ↓
MainView
      ↓
Productos registrados
```

De esta manera se mantiene la separación de responsabilidades entre los archivos de datos, los servicios y la interfaz gráfica.

## Funcionamiento de los usuarios

Los usuarios se encuentran almacenados en `datos/usuarios.json`.

El proceso de validación es:

```text
usuarios.json
      ↓
ArchivoServicio
      ↓
RestauranteServicio
      ↓
LoginView
      ↓
Usuario + contraseña
      ↓
Validación
```

Si las credenciales coinciden con un usuario registrado, la aplicación permite ingresar a la interfaz principal.

## Interfaz gráfica

La aplicación utiliza una única ventana principal de Tkinter.

La primera pantalla corresponde al inicio de sesión. Después de una autenticación correcta, se cambia a la interfaz principal sin crear una segunda ventana principal.

Las vistas se comunican con los servicios para obtener la información necesaria.

## Ejecución

Para ejecutar el proyecto se debe abrir una terminal en la carpeta principal de `restaurante_app` y utilizar:

```bash
python main.py
```

También puede utilizarse:

```bash
py main.py
```

dependiendo de la configuración de Python del equipo.

## Comprobaciones realizadas

La aplicación permite comprobar:

* Inicio correcto de la aplicación.
* Visualización de la pantalla de acceso.
* Ingreso de usuario y contraseña.
* Validación de campos vacíos.
* Validación de credenciales incorrectas.
* Acceso con credenciales válidas.
* Visualización de productos registrados.
* Visualización de usuarios registrados.
* Lectura de información mediante los servicios.
* Cierre de sesión.
* Regreso al LoginView dentro de la misma ventana principal.

## Funcionalidades pendientes

En esta etapa no se implementan todavía todas las funcionalidades de la versión de consola.

La opción de **Ventas** se mantiene identificada como funcionalidad pendiente y será desarrollada progresivamente en las siguientes semanas.

También se podrán incorporar posteriormente otras operaciones del restaurante conforme avancen los contenidos de la asignatura.

## Conclusión

La Semana 13 permitió iniciar la transición de `restaurante_app` desde una aplicación de consola hacia una aplicación con interfaz gráfica utilizando Tkinter.

La estructura implementada mantiene la separación de responsabilidades mediante modelos, servicios, archivos JSON y vistas gráficas. Esto permite que el proyecto pueda continuar creciendo sin concentrar toda la lógica en un solo archivo.

La aplicación cuenta con una pantalla de acceso, validación de usuarios, una interfaz principal y consulta de productos y usuarios registrados, dejando preparada la base para incorporar nuevas funcionalidades en las siguientes semanas.
