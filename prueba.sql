-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2023 a las 01:39:20
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Contacto` varchar(50) NOT NULL,
  `Dirección` varchar(100) NOT NULL,
  `Ocupación` varchar(50) NOT NULL,
  `Rut` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `Nombre`, `Apellido`, `Contacto`, `Dirección`, `Ocupación`, `Rut`) VALUES
(1, 'Pepe', 'wall', 'juanperez@ina.com', 'Calle 123', 'Alumno', '20365835-4'),
(2, 'María', 'López', 'marialopez@ina.com', 'Avenida 465', 'Alumno', '19364838-4'),
(3, 'Carlos', 'González', 'carlosgonzalez@ina.com', 'Plaza 789', 'Alumno', '19273935-6'),
(4, 'Laura', 'García', 'lauragarcia@ina.com', 'Calle 643', 'Alumno', '20467427-2'),
(5, 'Pedro ', 'Ramírez', 'pedroramirez@ina.com', 'Avenida 273', 'Alumno', '23745482-7'),
(6, 'Ana', 'Martínez', 'anamartinez@ina.com', 'Plaza 123', 'Docente', '19382735-3'),
(7, 'Claudio', 'Hérnandez', 'claudiohernandez@ina.com', 'Calle 837', 'Docente', '19373728-5'),
(8, 'Sofía', 'Silva', 'sofiasilva@ina.com', 'Avenida 349', 'Docente', '18372637-9'),
(9, 'Felipe', 'Torres', 'felipetorres@ina.com', 'Plaza 473', 'Docente', '17294639-3'),
(10, 'Cecilia', 'Gómez', 'ceciliagomez@ina.com', 'Calle 927', 'Docente', '18273628-6');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `id_libro` int(11) NOT NULL,
  `Titulo_libro` varchar(100) NOT NULL,
  `Cantidad` int(3) NOT NULL,
  `Autor` varchar(100) NOT NULL,
  `Tipo` varchar(50) NOT NULL,
  `Código` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`id_libro`, `Titulo_libro`, `Cantidad`, `Autor`, `Tipo`, `Código`) VALUES
(1, 'El Gran Gatsby', 5, 'F. Scott Fitzgerald', 'Novela', 12345678),
(2, '1984', 3, 'George Orwell', 'Distopía', 65423827),
(3, 'Cien años de soledad', 8, 'Gabriel García Márquez', 'Realismo mágico', 92737284),
(4, 'Orgullo y prejuicio', 6, 'Jane Austen', 'Novela romántica', 82649367),
(5, 'Don Quijote de la Mancha', 4, 'Miguel de Cervantes Saavedra', 'Novela', 83562837),
(6, 'La Odisea', 2, 'Homero', 'Poema épico', 92748362),
(7, 'Harry Potter y la piedra filosofal', 10, 'J. K. Rowling', 'Fantasía', 38472937),
(8, 'El señor de los anillos', 7, 'J. R. R. Tolkien', 'Fantasía', 83746283),
(9, 'Crónica de una muerte anunciada', 3, 'Gabriel García Márquez', 'Realismo', 63827394),
(10, 'Matar a un ruiseñor', 5, 'Harper Lee', 'Novela', 72638273),
(14, 'Como ser el ma chister', 4, 'mr chukap', 'risas', 123456767);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `id_prestamo` int(11) NOT NULL,
  `Rut_cliente` varchar(10) NOT NULL,
  `Estado_libro` varchar(50) NOT NULL,
  `Fecha_prestamo` date NOT NULL,
  `Fecha_entrega` date NOT NULL,
  `Titulo_libro` varchar(100) NOT NULL,
  `codigo` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`id_prestamo`, `Rut_cliente`, `Estado_libro`, `Fecha_prestamo`, `Fecha_entrega`, `Titulo_libro`, `codigo`) VALUES
(2, '19365838-4', 'Al día', '2023-06-03', '2023-08-06', '1984', 0),
(3, '19273935-6', 'Retrasado', '2023-06-01', '2023-06-12', 'Matar a un ruiseñor', 0),
(4, '20467427-2', 'Retrasado', '2023-06-03', '2023-06-14', 'Crónica de una muerte anunciada', 0),
(5, '23745482-7', 'Retrasado', '2023-06-08', '2023-06-17', 'El señor de los anillos', 0),
(6, '19382735-3', 'Al día', '2023-06-04', '2023-08-14', 'Cien años de soledad', 0),
(7, '19373728-5', 'Al día', '2023-06-08', '2023-08-20', 'Orgullo y prejuicio', 0),
(8, '18372637-9', 'Retrasado', '2023-06-01', '2023-06-23', 'Don Quijote de la Mancha', 0),
(10, '18273628-6', 'Al día', '2023-06-07', '2023-08-22', 'Harry Potter y la piedra filosofal', 0),
(12, '18273628-6', 'al dia', '2023-07-08', '2023-07-28', 'el libro mas chister', 2333345),
(14, '20365835-4', 'al dia', '2023-07-08', '2023-07-15', 'como ser chister ', 1234567786),
(15, '20365835-4', 'al dia', '2023-07-08', '2023-07-15', 'como dejar de ser chister ', 123456753);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`id_libro`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`id_prestamo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `id_libro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `id_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
