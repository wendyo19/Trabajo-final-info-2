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
    
    def parte_del_cerebro(self):
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
    
    
    