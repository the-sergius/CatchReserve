from fastapi import FastAPI, Response
import mysql.connector
from pydantic import BaseModel
class Establecimiento(BaseModel):
    nombre_establecimiento: str
    direccion_establecimiento: str
    telefono_establecimiento: str

class Servicio(BaseModel):
    id_establecimiento: str
    nombre_servicio: str
    descripcion_servicio: str

class Reserve(BaseModel):
    id_user: str
    id_service: str
    reserve_date: str
    reserve_time: str

class User(BaseModel):
    username: str
    surname: str
    email: str
    password: str

app = FastAPI()

@app.get("/establecimientos/")
def main():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM establecimientos")
        establecimientos = cursor.fetchall()
        data = {
            "establecimientos": establecimientos
        }
        return data
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error conectando a MySQL"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.get("/servicios/")
def main():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM servicios")
        servicios = cursor.fetchall()
        data = {
            "servicios": servicios
        }
        return data
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error conectando a MySQL"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.get("/reserves/")
def main():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM servicios")
        reserves = cursor.fetchall()
        data = {
            "reserves": reserves
        }
        return data
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error conectando a MySQL"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")


@app.get("/users/")
def main():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall()
        data = {
            "users": users
        }
        return data
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error conectando a MySQL"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.post("/makeReserve/")
def make_reserve(reserve: Reserve):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO reservas (id_usuario, id_servicio, fecha_reserva, hora_reserva) VALUES (%s, %s, %s, %s)"        
        val = (reserve.id_user, reserve.id_service, reserve.reserve_date, reserve.reserve_time)
        cursor.execute(sql, val)
        conexion.commit()
        return {"message": "Reserva realizada correctamente"}
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error al crear el servicio"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.post("/addService/")
def create_servicio(servicio: Servicio):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO servicios (id_establecimiento, nombre_servicio, descripcion_servicio) VALUES (%s, %s, %s)"        
        val = (servicio.id_establecimiento, servicio.nombre_servicio, servicio.descripcion_servicio)
        cursor.execute(sql, val)
        conexion.commit()
        return {"message": "Servicio creado correctamente"}
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error al crear el servicio"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.post("/addEstablecimiento/")
def create_establecimiento(establecimiento: Establecimiento):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO establecimientos (nombre_establecimiento, direccion_establecimiento, telefono_establecimiento) VALUES (%s, %s, %s)"
        val = (establecimiento.nombre_establecimiento, establecimiento.direccion_establecimiento, establecimiento.telefono_establecimiento)
        cursor.execute(sql, val)
        conexion.commit()
        return {"message": "Establecimiento creado correctamente"}
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error al crear el establecimiento"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

@app.post("/createUser/")
def create_user(user: User):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="catchreserve"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre_usuario, apellido_usuario, email_usuario, password_usuario) VALUES (%s, %s, %s, %s)"
        val = (user.username, user.surname, user.email, user.password)
        cursor.execute(sql, val)
        conexion.commit()
        return {"message": "Usuario creado correctamente"}
    except mysql.connector.Error as error:
        return Response(status_code=500, content={"error": "Error al crear el usuario"}, media_type="application/json")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")