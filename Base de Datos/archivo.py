import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="C751627C4C4C6790FE2F900B395A3CA9",
    database="prueba"
)
cursor = midb.cursor()
#cursor.execute('select * from usuario')

#Insert
#sql = "insert into usuario (email, username, edad) values (%s, %s, %s)"
#values = ("juanito@gmail.com","juanito", 55)
#resultado = cursor.fetchall() #Me permite traer todos los registros de la base de datos
#resultado = cursor.fetchone() #Me permite traer solo el primer resultado

#Update
#sql = "update usuario set email = %s where id=%s"
#values = ("pepitogranda@gmail.com", '3')
#cursor.execute(sql, values)
#midb.commit()

#Delete
#sql = "delete from usuario where id=%s"
#values = (3,)
#cursor.execute(sql, values)
#midb.commit()

#Limite
cursor.execute("select * from usuario limit 1")
resultado = cursor.fetchall()
print(resultado)
#print(cursor.rowcount)