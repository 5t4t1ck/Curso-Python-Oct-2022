create database prueba; #Crea la base de datos prueba
drop database prueba; #Elimina la base de datos prueba
use prueba; #Indicamos a MySQL que estamos utilizando la base de datos prueba

#Crear la tabla usuario, creamos los campos id
# creamos el campo email de tipo varchar, creamos el campo username
create table usuario(id int, email varchar(255), username varchar(50)); #Se puede utilizar primary key auto_increment en el campo id 
drop table usuario; #Elimina la tabla usuario

#Crear el campo edad en la Tabla usuario
alter table usuario add edad int; #Altera la tabla agregando el campo edad

# Eliminar el campo edad en la Tabla Usuario
alter table usuario drop column edad;

#Modificar tabla
alter table usuario modify column email varchar(50);

# Insertar Registros
insert into usuario (email, username) 
values ('dsaavedra88@gmail.com','statick');

#Eliminar registros
delete from usuario where email = 'dsaavedra88@gmail.com' limit 1;

alter table usuario add primary key (id); # Agregamos el campo id como primary key
alter table usuario modify column id int auto_increment; # Agregamos el campo id como auto_increment

select * from usuario; #Muestra todas las columnas de la tabla

#Insertamos un nuevo registro
insert into usuario (email, username) 
values ('usuario@gmail.com','statick');

#Filtramos la busqueda de registro por el campo email
select * from usuario where email='usuario@gmail.com';

#Filtramos la búsqueda por una condición
select * from usuario where edad <= 31;

#Update
update usuario set edad = 32 where id = '1';

#Delete

delete from usuario where id='1';
