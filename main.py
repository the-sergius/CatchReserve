from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

class Establecimiento(BaseModel):
    nombre_establecimiento: str
    direccion_establecimiento: str
    telefono_establecimiento: str

app = FastAPI()

@app.get("/")
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

@app.post("/establecimientos/")
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
        val = (nombre_establecimiento, direccion_establecimiento, telefono_establecimiento)
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
