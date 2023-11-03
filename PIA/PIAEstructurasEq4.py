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
        print("La base de datos Ventas_DelSol y las tablas Productos, Sucursales y Ventas se han creado correctamente")
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    finally:
        
        if 'conn' in locals():
            conn.close()

Crear_tabla()

def mostrar_menu():
    while True:
        print("Base de Datos VENTAS DELSOL:")
        print("1. Registrar Producto")
        print("2. Registrar Sucursal")
        print("3. Registrar Venta")
        print("4. Salir del Programa")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            registrar_sucursal()
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            print(f"Hasta luego 😃")
            break
        else:
            print("ERROR: Opción no válida. Intentar nuevamente.")

def registrar_producto():
    try:
        conn = sqlite3.connect('Ventas_DelSol.db') 
        mi_cursor = conn.cursor()
        mi_cursor.execute("INSERT INTO Productos VALUES (1, 'Pluma', 15)")
        print("Producto registrado correctamente.")
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    finally:
        
        if 'conn' in locals():
            conn.close()

def registrar_sucursal():
    try:
        conn = sqlite3.connect('Ventas_DelSol.db') 
        mi_cursor = conn.cursor()
        mi_cursor.execute("INSERT INTO Sucursales VALUES (1, 'Guadalupe', '67190, Av. Pablo Livas 7601, Agua Nueva, 67193 Guadalupe, N.L.', 8003755260)")
        print("Sucursal registrada correctamente.")
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    finally:
        
        if 'conn' in locals():
            conn.close()

def registrar_venta():
    try:
        conn = sqlite3.connect('Ventas_DelSol.db') 
        mi_cursor = conn.cursor()
        mi_cursor.execute("INSERT INTO Ventas VALUES (1, 'Pluma', 'Guadalupe', 2, 15, 30, '02/11/2023')")
        print("Venta registrada correctamente.")
    except sqlite3.Error as e:
        print(e)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")
    finally:
        
        if 'conn' in locals():
            conn.close()

mostrar_menu()
