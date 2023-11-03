import random as rd
import sys
import datetime
import sqlite3 
from sqlite3 import Error
from datetime import (date, datetime, timedelta)
import openpyxl

def Crear_tabla():
    try:
        conn = sqlite3.connect('Ventas_DelSol.db') 
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Productos (idProducto INT PRIMARY KEY, nombreProducto TEXT NOT NULL, precioProducto INT NOT NULL)")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Sucursales (idSucursal INT PRIMARY KEY, nombreSucursal TEXT NOT NULL, direccionSucursal TEXT NOT NULL, telefonoSucursal INT NOT NULL)")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS Ventas (idVenta INT PRIMARY KEY, producto TEXT NOT NULL, sucursal TEXT NOT NULL, cantidadProducto INT NOT NULL, costoProducto INT NOT NULL, costoTotal INT NOT NULL, fecha TEXT NOT NULL)")
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

Crear_tabla()