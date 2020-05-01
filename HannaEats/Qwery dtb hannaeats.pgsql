INSERT INTO food_alimento (nombre, descripcion, precio,foto)
VALUES ('Taco Bisteck','Taco de Bisteck de Res',18,'/food/images/TdB.png');

INSERT INTO food_status (status)
VALUES ('Recibida');

INSERT INTO food_status (status)
VALUES ('Preparandose');

INSERT INTO food_status (status)
VALUES ('En espera');

INSERT INTO food_status (status)
VALUES ('En camino');

INSERT INTO food_status (status)
VALUES ('Entregada');

INSERT INTO food_status (status)
VALUES ('Finalizada');

INSERT INTO food_status (status)
VALUES ('Cancelada');

INSERT INTO food_alimento (nombre, descripcion, precio,foto)
VALUES ('Taco Pastor','Taco de Pastor',20,'/food/images/TdP.png');

INSERT INTO users_cliente (nombre,ap_paterno,ap_materno,correo,telefono)
VALUES ('Pablo','Millan','Pimentel','pmp@gmail.com',4564564);

INSERT INTO users_repartidor (nombre,ap_paterno,ap_materno,correo,telefono)
VALUES ('Fernando','Millan','Pimentel','drs@gmail.com',678565);

INSERT INTO users_cliente_direccion (cliente_id,direcciones_id)
VALUES (1,1);

INSERT INTO food_ordencomida (calificacion,id_cliente_id,id_repartidor_id,status_id)
VALUES (1,1,1,4);

INSERT INTO food_cantidadalimento (cantidad,alimento_id,orden_id)
VALUES (3,1,1);

INSERT INTO food_cantidadalimento (cantidad,alimento_id,orden_id)
VALUES (5,2,1);

SELECT * FROM food_ordencomida;
SELECT * FROM food_alimento;
SELECT * FROM food_status;

SELECT * FROM users_direcciones;
SELECT * FROM users_repartidor;
SELECT * FROM users_cliente_direccion;
SELECT * FROM users_cliente;

SELECT * FROM food_cantidadalimento;