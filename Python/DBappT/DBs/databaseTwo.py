
import pdb
from mysql.connector import Error
from prettytable import PrettyTable

from DBs.conectDB import ConnectDB


class DBappTextend(ConnectDB):
    
    def __init__(self, db_app):
        self.con = db_app.con 
        try:
            with self.con.cursor() as cursor:
                cursor.execute("USE ShopSt")
                cursor.execute("SELECT DATABASE();")
                active_db = cursor.fetchone()
                print(f"Base de datos activa: {active_db[0]}")
        except Error as err:
            print(f"Error al intentar usar la base de datos: {err}")  

    def insert_data_product(self, data):
        try:
            if not data['name'] or not data['price'] or not data['stock']:
                raise ValueError("Los campos NOMBRE, PRECIO, STOCK son obligatorios no pueden estar vacios.")

            with self.con.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Productos (NOMBRE, PRECIO, STOCK)
                VALUES (%s, %s, %s)
                """,(data['name'], data['price'], data['stock']))
                self.con.commit()
                print("[+] Producto insertado con exito.")
        except Error as err:
            print(f"Error al ejecutar al insercion de la data: {err}")

    def insert_data_registration(self, data):
        try:
            if not data['id_product'] or not data['stock']:
                raise ValueError("Los campos ID_PRODUCTO, CANTIDAD son obligatorios no pueden estar vacios.")

            with self.con.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Registro_ventas (ID_PRODUCTO, CANTIDAD)
                VALUES (%s, %s)
                """,(data['id_product'], data['stock']))
                self.con.commit()
                print("[+] Venta Registrada con exito.")
        except Error as err:
            print(f"Error al ejecutar al insercion de la data: {err}")

    def total_sales(self):
        try:
            with self.con.cursor(buffered=True) as cursor:
                cursor.callproc("cal_total_ventas")
                cursor.nextset()
                result = cursor.stored_results()
                for values in result:
                    data = values.fetchall()
                    if data:
                        table = PrettyTable([i[0] for i in values.description])
                        for row in data:
                            table.add_row(row)
                        print(table)
        except Error as err:
            print(f"Error al ejecutar la consulta: {err}")

    def stock_product(self, id):
        try:
            with self.con.cursor(buffered=True) as cursor:
                cursor.execute("SELECT obtener_stock_producto(%s) AS STOCK", (id,))
                result = cursor.fetchall()
                if result:
                    table = PrettyTable([i[0] for i in cursor.description])
                    for row in result:
                        table.add_row(row)
                    print(table)
        except Error as err:
            print(f"Error al ejecutar la consulta: {err}")
    
    def update_stock_product(self, data):
        try:
            if not data['id_product'] or not data['stock']:
                raise ValueError("Los campos ID_PRODUCTO, CANTIDAD son obligatorios no pueden estar vacíos.")

            with self.con.cursor() as cursor:
                cursor.callproc('actualizar_stock', (data['id_product'], data['stock']))
                while cursor.nextset():
                    pass
                self.con.commit()
                print("[+] Stock actualizado con éxito")
        except Error as err:
            print(f"Error al ejecutar la consulta: {err}")
    
    def different_query(self, query):
        try:
            with self.con.cursor() as cursor:
                cursor.execute(query)
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except Error as err:
            print(f"Error al ejecutar la consulta: {err}")  

