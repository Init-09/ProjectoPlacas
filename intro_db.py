import pymysql

class DataBase:
    def __init__(self):
        self.connection=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='uth'
        )
        self.cursor = self.connection.cursor()
        print("--------------")
        print("Conexion Exitosa!!!")
        print("#################")

    def get_all_records(self):
        sql='select * from alumno'
        try:
            self.cursor.execute(sql)
            Alums=self.cursor.fetchall()
            print("Id  | Nombre ")
            print("______________")
            for alum in Alums:
                print(alum[0],"  | ",alum[1])
            print("#################")
        except Exception as e:
            raise 
    
    def get_one_record(self,Id):
        sql='select * from alumno where Code={}'.format(Id)
        try:
            self.cursor.execute(sql)
            Alum = self.cursor.fetchone()
            print("_______________")
            print("Codigo:",Alum[0])
            print("Nombre:",Alum[1])
            print("Email:",Alum[2])
            print("_______________")
        except Exception as e:
            raise

    def show_one_record(self,nombre):
        sql='select * from alumno where Name="{}"'.format(nombre)
        try:
            self.cursor.execute(sql)
            Alum = self.cursor.fetchone()
            print("_______________")
            print("Codigo:",Alum[0])
            print("Nombre:",Alum[1])
            print("Email:",Alum[2])
            print("_______________")
        except Exception as e:
            raise
    def insert_one_record(self,ide,nombre,mail):
        sql = "INSERT INTO alumno (Code,Name,email) VALUES ({},'{}','{}')".format(ide,nombre,mail)       
        try:       
            self.cursor.execute(sql)
            self.connection.commit()
            print(self.cursor.rowcount, "record inserted.")
            sql='select * from alumno'
            try:
                self.cursor.execute(sql)
                Alums=self.cursor.fetchall()
                print("Id  | Nombre ")
                print("______________")
                for alum in Alums:
                    print(alum[0],"  | ",alum[1])
                print("#################")
            except Exception as e:
                raise
        except Exception as e:
            raise

    def edit_one_record(self,mail,ide):
        sql = "update alumno set email='{}' where Code={}".format(mail,ide)       
        try:       
            self.cursor.execute(sql)
            self.connection.commit()
            print(self.cursor.rowcount, "record inserted.")
            sql='select * from alumno'
            try:
                self.cursor.execute(sql)
                Alums=self.cursor.fetchall()
                print("Id  | Nombre ")
                print("______________")
                for alum in Alums:
                    print(alum[0],"  | ",alum[1])
                print("#################")
            except Exception as e:
                raise
        except Exception as e:
            raise

obj_db1 = DataBase()
#obj_db1.get_all_records()
#obj_db1.get_one_record(1)
obj_db1.show_one_record('Axel')
# ide=input("Ingrese id: ")
# nombre=input("Ingrese nombre: ")
# mail=input("Ingrese mail: ")
# int(float(ide))
# obj_db1.edit_one_record(mail,ide)



