import mysql.connector

class Vender:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost",user="root",passwd="lupita11",database="productos")
    
    def __str__(self):
        datos=self.consulta_productos()
        aux=''
        for fila in datos:
            aux += str(fila)+"\n"
        return aux

    def consulta_productos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Ventas")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def buscar_productos(self):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM Ventas WHERE id = {}".format(id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_productos(self,codigo,producto,grupo,precio):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO Ventas (codigo,producto,grupo,precio) VALUES('{}','{}','{}','{}')'''.format(codigo,producto,grupo,precio)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    
    def elimina_productos(self,id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Ventas WHERE id = {}'''.format(id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    
    def editar_productos(self,id,codigo,producto,grupo,precio):
        cur = self.cnn.cursor()
        sql='''UPDATE Ventas SET codigo='{}',producto='{}',grupo='{},precio='{}' WHERE id={}'''.format(codigo,producto,grupo,precio,id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

