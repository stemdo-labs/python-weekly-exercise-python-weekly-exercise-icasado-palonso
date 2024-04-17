### ENTREGABLE 2.

*"Desarrollo de una Aplicación Web de To-Do List con Docker y FastApi"* 

Este proyecto integrará los fundamentos de DevOps, el uso de herramientas colaborativas, programación en Python, y la creación y gestión de contenedores con Docker.

## Descripción del Proyecto ##

Los participantes desarrollarán una aplicación web de lista de tareas (To-Do List) utilizando FastApi, un micro framework de Python para desarrollo web. La aplicación permitirá a los usuarios crear, leer, actualizar y eliminar tareas. Este proyecto se contenerizará usando Docker, facilitando su despliegue y escalabilidad.

## Objetivos

-   Practicar la programación en Python utilizando FastApi para el desarrollo backend.
    
-   Aplicar conocimientos de Docker para contenerizar la aplicación.
    
-   Fomentar la colaboración utilizando herramientas como GitHub para el control de versiones y Microsoft Teams para la comunicación.
    
-   Implementar conceptos de DevOps en el ciclo de vida del desarrollo del software, desde la codificación hasta el despliegue.
    

## Especificaciones del Proyecto

-   Desarrollo Backend con FastApi:
    
    -   Implementar CRUD (Create, Insert, Delete, Update) para las tareas.
    
    -   Utilizar la biblioteca necesaria de python para realizar la conexión con la base de datos utilizada.
    
-   Dockerización de la Aplicación:
    
    -   Crear un Dockerfile para contenerizar la base de datos utilizada.
    

    -   Utilizar Docker Compose para gestionar la aplicación y cualquier servicio adicional si es necesario.
    
    -   Podéis usar cualquier imagen de bases de datos, preferible postgres que es la que menos pesa.
    
-   Ejecución del aplicativo
    
    -   Usar uvicorn para servir el aplicativo en la máquina local (localhost)
    
-   Colaboración y Control de Versiones
    
    -   Uso Integrado de Microsoft Teams, Planner y GitHub:
    
    -   Los participantes utilizarán Microsoft Teams para la comunicación en tiempo real, incluidas las discusiones de desarrollo, reuniones diarias de sincronización y sesiones de problem-solving.
    
    -   Microsoft Planner será implementado para la organización de tareas y la asignación de responsabilidades dentro del equipo. Cada tarea en Planner estará vinculada a una tarea o issue en GitHub Projects, asegurando una integración fluida entre la planificación del proyecto y el trabajo técnico.
    
    -   Se utilizará GitHub Projects para seguir el progreso del desarrollo, administrar issues, y priorizar el trabajo. Esta herramienta estará directamente conectada con el repositorio de GitHub, facilitando la visibilidad de la contribución de cada miembro del equipo y el estado del desarrollo.
    

-   Desarrollo Colaborativo con GitHub:
    
    -   Implementación de Pull  Requests para la integración de características y revisiones de código, promoviendo las mejores prácticas de desarrollo colaborativo.
    
    -   Uso de issues de GitHub para rastrear bugs, solicitudes de características y tareas generales del proyecto, asegurando que todos los miembros del equipo estén alineados con los objetivos y prioridades.
    

## Documentación y Entrega:

    -   Documentación Detallada:
    
        -   El proyecto debe incluir una documentación comprensiva del proceso de desarrollo, la configuración de herramientas (Docker, FastApi), y cómo se utilizó la integración entre Microsoft Teams, Planner, y GitHub Projects para gestionar el proyecto.
    
        -   El README.md del repositorio de GitHub deberá contener instrucciones claras sobre cómo configurar y ejecutar la aplicación, incluyendo la configuración de Docker y cualquier dependencia necesaria.
    
    -   Presentación del Proyecto:
    
        -   Al final del desarrollo, se realizará una presentación donde cada equipo demostrará su aplicación. Durante esta presentación, se destacará cómo la integración entre las herramientas de colaboración y control de versiones facilitó el éxito del proyecto.
    

Esta estructura enfatiza no solo en el desarrollo técnico, sino también las habilidades de gestión de proyectos y trabajo en equipo, utilizando herramientas modernas de colaboración y control de versiones. Este enfoque integral prepara a los participantes para el entorno colaborativo y técnico de DevOps en el mundo profesional.ENTREGABLE 2.

"Desarrollo de una Aplicación Web de To-Do List con Docker y FastApi"

Este proyecto integrará los fundamentos de DevOps, el uso de herramientas colaborativas, programación en Python, y la creación y gestión de contenedores con Docker.

## Datos extra
Para el correcto funcionamiento de la base de datos, tendremos que crear una tabla con sus diferentes columnas con los datos siguientes, para todos poder realizar las consultas sobre la misma tabla. 

La tabla contendrá columnas y datos dados, que son los siguientes:

```CREATE TABLE personas (
  id INTEGER PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  edad INTEGER,
  fecha_nacimiento DATE
);

INSERT INTO personas (id, nombre, apellido, edad, fecha_nacimiento)
VALUES
  (1, 'Juan', 'Perez', 25, '2000-01-01'),
  (2, 'Maria', 'Garcia', 30, '1994-05-10'),
  (3, 'Pedro', 'Rodriguez', 18, '2006-12-25'),
  (4, 'Ana', 'Lopez', 22, '1992-07-04'),
  (5, 'Jose', 'Martinez', 35, '1989-09-15'),
  (6, 'Laura', 'Gonzalez', 28, '1996-03-20'),
  (7, 'Carlos', 'Sanchez', 20, '2004-11-08'),
  (8, 'Sofia', 'Hernandez', 19, '2005-06-12'),
  (9, 'David', 'Diaz', 27, '1997-02-14'),
  (10, 'Andrea', 'Ruiz', 23, '1991-10-27');