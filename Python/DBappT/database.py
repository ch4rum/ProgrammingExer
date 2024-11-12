#!/usr/bin/env python3 

import getpass
import mysql.connector
from encrypt import *
from prettytable import PrettyTable

class DBappT:
    def __init__(self, username, password_b64, encryption_key):
        self.username = username
        self._encryption_key = encryption_key
        self.necrypt = EncryptPass(encryption_key)
        self._encrypted_password_b64 = self.necrypt.set_encrypt_pass(password_b64)
        self.con = self._conect_db()

    def _conect_db(self):
        decrypted_password = self.necrypt.get_decrypt_pass(self._encryption_key)
        conexion = mysql.connector.connect(
            host="localhost", 
            user=self.username,
            password=decrypted_password, 
            database="UnirDB", 
            charset="utf8mb4",  
            collation="utf8mb4_unicode_ci"
        )
        return conexion 

    def close(self):
        if self.con.is_connected():
            self.con.close()

    def insert_data_client(self, data):
        try:
            if not data['name'] or not data['lastName1'] or not data['city'] or not data['category']:
                raise ValueError("Los campos NOMBRE, APELLIDO1, CIUDAD Y CATEGORIA son obligatorios no pueden estar vacios.")

            with self.con.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Cliente (NOMBRE, APELLIDO1, APELLIDO2, CIUDAD, CATEGORIA)
                VALUES (%s, %s, %s, %s, %s)
                """,(data['name'], data['lastName1'], data['lastName2'] if data['lastName2'] is not None else None, data['city'], data['category']))
                self.con.commit()
                print("[+] Cliente insertado con exito.")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar al insercion de la data: {err}")

    def insert_data_order(self, data):
        try:
            if not data['total'] or not data['date'] or not data['id_client'] or not data['id_commercial']:
                raise ValueError("Los campos TOTAL, FECHA, ID_CLIENTE y ID_COMERCIAL son obligatorios no pueden estar vacios.")

            with self.con.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Pedidos (TOTAL, FECHA, ID_CLIENTE, ID_COMERCIAL)
                VALUES (%s, %s, %s, %s)
                """,(data['total'], data['date'], data['id_client'], data['id_commercial']))
                self.con.commit()
                print("[+] Pedido insertado con exito.")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar al insercion de la data: {err}")

    def insert_data_commercial(self, data):
        try:
            if not data['name'] or not data['lastName1'] or not data['lastName2'] or not data['commision']:
                raise ValueError("Los campos NOMBRE,  APELLIDO1, APELLIDO2 y COMISION son obligatorios no pueden estar vacios.")

            with self.con.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Comercial (NOMBRE,  APELLIDO1, APELLIDO2, COMISION)
                VALUES (%s, %s, %s, %s)
                """,(data['name'], data['lastName1'], data['lastName2'], data['commission']))
                self.con.commit()
                print("[+] Comercial insertado con exito.")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar al insercion de la data: {err}")

    def date_order(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute("SELECT * FROM Pedidos ORDER BY FECHA DESC;")
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")

    def range_order(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute("SELECT * FROM Pedidos p WHERE p.TOTAL BETWEEN 300 AND 600 ORDER BY p.FECHA ASC;")
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
    
    def client_two_null(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute("SELECT ID, NOMBRE, APELLIDO1 FROM Cliente WHERE APELLIDO2 IS NULL ORDER BY APELLIDO1 ASC, NOMBRE ASC;")
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
    
    def client_realized_order(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute('''
                SELECT DISTINCT Cliente.ID, Cliente.NOMBRE, Cliente.APELLIDO1, Cliente.APELLIDO2 
                FROM Cliente
                JOIN Pedidos ON Cliente.ID = Pedidos.ID_CLIENTE 
                ORDER BY Cliente.APELLIDO1 COLLATE utf8mb4_unicode_ci ASC, 
                         Cliente.APELLIDO2 COLLATE utf8mb4_unicode_ci ASC,
                         Cliente.NOMBRE COLLATE utf8mb4_unicode_ci ASC; 
                ''')
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")

    def commercial_sales_to_maria(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute('''
                SELECT DISTINCT Comercial.NOMBRE, Comercial.APELLIDO1, Comercial.APELLIDO2 
                FROM Comercial
                JOIN Pedidos ON Comercial.ID = Pedidos.ID_COMERCIAL
                JOIN Cliente ON Pedidos.ID_CLIENTE = Cliente.ID
                WHERE Cliente.NOMBRE = 'Marià'
                    AND Cliente.APELLIDO1 = 'Santana'
                    AND Cliente.APELLIDO2 = 'Moreno';
                ''')
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")

    def created_view_order(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute("DROP VIEW IF EXISTS ResumenPedidos;")
                cursor.execute('''
                CREATE VIEW IF NOT EXISTS `ResumenPedidos` AS
                SELECT 
                    Pedidos.ID AS Pedido_ID, 
                    Cliente.NOMBRE AS Cliente_Nombre,
                    CONCAT(Cliente.APELLIDO1, ' ', IFNULL(Cliente.APELLIDO2,'')) AS Cliente_Apellidos, 
                    Comercial.NOMBRE AS Comercial_Nombre,
                    CONCAT(Comercial.APELLIDO1, ' ', Comercial.APELLIDO2) AS Comercial_Apellidos,
                    Pedidos.TOTAL AS Pedidos_Total 
                FROM Pedidos
                JOIN Cliente ON Pedidos.ID_CLIENTE = Cliente.ID
                JOIN Comercial ON Pedidos.ID_COMERCIAL = Comercial.ID;
                ''')
                cursor.execute("SELECT * FROM ResumenPedidos;")
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")   

    def total_sales(self):
        try:
            with self.con.cursor() as cursor:
                cursor.execute('''
                SELECT 
                    Comercial_Nombre, Comercial_Apellidos,
                    SUM(Pedidos_Total) AS Total_Ventas, 
                    AVG(Pedidos_Total) AS Promedio_Ventas, 
                    COUNT(Pedido_ID) AS Cantidad_Pedidos
                FROM ResumenPedidos
                GROUP BY Comercial_Nombre, Comercial_Apellidos
                ORDER BY Total_Ventas DESC;
                ''')
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")  


    def different_query(self, query):
        try:
            with self.con.cursor() as cursor:
                cursor.execute(query)
                table = PrettyTable([i[0] for i in cursor.description])
                for row in cursor.fetchall():
                    table.add_row(row)
                print(table)
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")  
