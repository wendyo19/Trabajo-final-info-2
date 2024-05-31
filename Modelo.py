import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from sqlalchemy import create_engine

#conexion con la base de datos
engine = create_engine('mysql+pymysql://admin123:contrasena123@localhost/info2')

class modelo: 
    def __init__(self, nombre, definicion, enfermedad, sintomas, especialista, tratamiento, ID, id_enfermedad ):
        self.__login = ""
        self.__password = ""
        self.__ID = ID
        self.__id_enfermedad = id_enfermedad
        self.__parte_del_cerebro = nombre
        self.__definicion = definicion
        self.__enfermedad = enfermedad
        self.__sintomas = sintomas
        self.__especialista = especialista
        self.__tratamiento = tratamiento

        self.__cnx = mysql.connector.connect(
            user='admin123', password='contrasena123', host='localhost', database='info2'
        )
        self.__cursor = self.__cnx.cursor()

    def setlogin(self, admin123):
        self.__login = admin123
    def setPassword(self, contrasena123):
        self.__password = contrasena123

    def Validar_usuario(self, admin123, contrasena123):
        return(self.__login == admin123) and (self.__password == contrasena123)
    
    def ID(self):
        return self.__ID
    
    def id_enfermedad(self):
        return self.__id_enfermedad
    
    def nombre(self):
        return self.__parte_del_cerebro
    
    def definicion(self):
        return self.__definicion
    
    def enfermedad(self):
        return self.__enfermedad
    
    def sintomas(self):
        return self.__sintomas
    
    def especialista(self):
        return self.__especialista
    
    def tratamiento(self):
        return self.__tratamiento
    
    def explorar(self, parte_seleccioanda):
        parte_seleccioanda = []
        for i in parte_seleccioanda:
            query = '''
                   SELECT g.nombre, g.descripcion, e.nombre, e.sintomas, e.espacilitas, e.tratamiento
                    FROM general g
                    INNER JOIN enfermedad e ON g.ID 0 e.ID
                     WHERE g.nombre = %s
                       '''
            self.__cursor.execute(query, (parte_seleccioanda))
            parte_seleccioanda.append(dict(self.__cursor.fetchone()))#extrae informacion de la tabla
        return parte_seleccioanda




modelo = modelo()
parte_seleccionada = modelo.explorar(["Cerebrum", "Cerebelo"])
for parte in parte_seleccionada:
    print(parte)
    print(f"Nombre: {parte['nombre']}")
    print(f"Descripción: {parte['descripcion']}")
    print(f"Enfermedad: {parte['nombre_enfermedad']}")
    print(f"Sintomas: {parte['sintomas']}")
    print(f"Especialista: {parte['especialista']}")
    print(f"Tratamiento: {parte['tratamiento']}")
    print(f"ID: {parte['ID']}")
    print(f"ID de enfermedad: {parte['id_enfermedad']}")
    print()