from fastapi import FastAPI, HTTPException
import psycopg2
 
app = FastAPI()
 
# Función para establecer la conexión a la base de datos
def connect_to_db():
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="to_do_list_db"
        )
        print("Conexión establecida correctamente a la base de datos")
        return connection
 
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None
 
# Ruta para obtener todas las tareas
@app.get("/tasks/")
def read_tasks():
    # Establecer conexión a la base de datos
    connection = connect_to_db()
 
    if connection:
        try:
            # Crear un cursor
            cursor = connection.cursor()
 
            # Consulta SQL para seleccionar todas las tareas
            query = "SELECT * FROM tasks;"
 
            # Ejecutar la consulta
            cursor.execute(query)
 
            # Obtener todas las filas
            tasks = cursor.fetchall()
 
            # Cerrar el cursor
            cursor.close()
 
            return tasks
 
        except (Exception, psycopg2.Error) as error:
            print("Error al obtener las tareas:", error)
            raise HTTPException(status_code=500, detail="Error al obtener las tareas.")
 
        finally:
            # Cerrar la conexión cuando hayamos terminado
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos.")
 
# Ruta para obtener una tarea por su ID
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # Establecer conexión a la base de datos
    connection = connect_to_db()
 
    if connection:
        try:
            # Crear un cursor
            cursor = connection.cursor()
 
            # Consulta SQL para seleccionar la tarea por su ID
            query = "SELECT * FROM tasks WHERE id = %s;"
 
            # Ejecutar la consulta con el ID como parámetro
            cursor.execute(query, (task_id,))
 
            # Obtener la tarea
            task = cursor.fetchone()
 
            if task:
                return task
            else:
                raise HTTPException(status_code=404, detail="Tarea no encontrada.")
 
        except (Exception, psycopg2.Error) as error:
            print("Error al obtener la tarea:", error)
            raise HTTPException(status_code=500, detail="Error al obtener la tarea.")
 
        finally:
            # Cerrar el cursor
            cursor.close()
 
            # Cerrar la conexión cuando hayamos terminado
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos.")
 
# Ruta para crear una nueva tarea
@app.post("/tasks/")
def create_new_task(title: str, description: str):
    # Establecer conexión a la base de datos
    connection = connect_to_db()
 
    if connection:
        try:
            # Crear un cursor
            cursor = connection.cursor()
 
            # Consulta SQL para insertar una nueva tarea
            query = "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING *;"
 
            # Ejecutar la consulta con los datos de la nueva tarea
            cursor.execute(query, (title, description))
 
            # Obtener la nueva tarea creada
            created_task = cursor.fetchone()
 
            # Confirmar los cambios en la base de datos
            connection.commit()
 
            return created_task
 
        except (Exception, psycopg2.Error) as error:
            print("Error al crear la tarea:", error)
            connection.rollback()
            raise HTTPException(status_code=500, detail="Error al crear la tarea.")
 
        finally:
            # Cerrar el cursor
            cursor.close()
 
            # Cerrar la conexión cuando hayamos terminado
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos.")
 
# Ruta para borrar una tarea por su ID
@app.delete("/tasks/{task_id}")
def delete_task_by_id(task_id: int):
    # Establecer conexión a la base de datos
    connection = connect_to_db()
 
    if connection:
        try:
            # Crear un cursor
            cursor = connection.cursor()
 
            # Consulta SQL para borrar una tarea por su ID
            query = "DELETE FROM tasks WHERE id = %s RETURNING *;"
 
            # Ejecutar la consulta con el ID como parámetro
            cursor.execute(query, (task_id,))
 
            # Obtener la tarea borrada
            deleted_task = cursor.fetchone()
 
            # Confirmar los cambios en la base de datos
            connection.commit()
 
            if deleted_task:
                return deleted_task
            else:
                raise HTTPException(status_code=404, detail="Tarea no encontrada.")
 
        except (Exception, psycopg2.Error) as error:
            print("Error al borrar la tarea:", error)
            connection.rollback()
            raise HTTPException(status_code=500, detail="Error al borrar la tarea.")
 
        finally:
            # Cerrar el cursor
            cursor.close()
 
            # Cerrar la conexión cuando hayamos terminado
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos.")