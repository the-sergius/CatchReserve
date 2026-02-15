CREATE DATABASE IF NOT EXISTS catchreserve;

USE catchreserve;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) NOT NULL,
    apellido_usuario VARCHAR(50) NOT NULL,
    email_usuario VARCHAR(50) NOT NULL UNIQUE,
    password_usuario VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS establecimientos (
    id_establecimiento INT AUTO_INCREMENT PRIMARY KEY,
    nombre_establecimiento VARCHAR(50) NOT NULL,
    direccion_establecimiento VARCHAR(100) NOT NULL,
    telefono_establecimiento VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    id_establecimiento INT NOT NULL,
    nombre_servicio VARCHAR(50) NOT NULL,
    descripción_servicio VARCHAR(200) NOT NULL,
    FOREIGN KEY (id_establecimiento) REFERENCES establecimientos(id_establecimiento)
);

CREATE TABLE IF NOT EXISTS reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_servicio INT NOT NULL,
    fecha_reserva DATE NOT NULL,
    hora_reserva TIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio)
);
