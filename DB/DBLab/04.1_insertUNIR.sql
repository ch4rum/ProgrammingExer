USE `UnirDB`

INSERT INTO `Comercial` (NOMBRE, APELLIDO1, APELLIDO2, COMISION)
VALUES
('Daniel', 'Sáez', 'Vega', 0.15),
('Juan', 'Gómez', 'López', 0.13),
('Diego', 'Flores', 'Salas', 0.11),
('Marta', 'Herrera', 'Gil', 0.14),
('Antonio', 'Carretero', 'Ortega', 0.12),
('Manuel', 'Domínguez', 'Hernández', 0.13),
('Antonio', 'Vega', 'Hernández', 0.11),
('Alfredo', 'Ruiz', 'Flores', 0.05);

INSERT INTO Cliente (ID, NOMBRE, APELLIDO1, APELLIDO2, CIUDAD, CATEGORIA) 
VALUES
(1, 'Aarón', 'Rivero', 'Gómez', 'Granada', 200),
(2, 'Adela', 'Salas', 'Díaz', 'Sevilla', 300),
(3, 'Adolfo', 'Rubio', 'Flores', 'Sevilla', 200),
(4, 'Adrián', 'Suárez', NULL, 'Jaén', 100),
(5, 'Marcos', 'Loyola', 'Médez', 'Almería', 100),
(6, 'Mariá', 'Santana', 'Moreno', 'Cádiz', 200),
(7, 'Pilar', 'Ruiz', NULL, 'Sevilla', 300),
(8, 'Pepe', 'Ruiz', 'Santana', 'Huelva', 200),
(9, 'Guillermo', 'López', 'Gómez', 'Granada', 225),
(10, 'Daniel', 'Santana', 'Loyola', 'Sevilla', 125);


INSERT INTO `Pedidos` (TOTAL, FECHA, ID_CLIENTE, ID_COMERCIAL)
VALUES
(150.5, STR_TO_DATE('05/10/2017', '%d/%m/%Y'), 5, 2),
(270.65, STR_TO_DATE('10/09/2016', '%d/%m/%Y'), 1, 5),
(65.26, STR_TO_DATE('05/10/2017', '%d/%m/%Y'), 2, 1),
(110.5, STR_TO_DATE('17/08/2016', '%d/%m/%Y'), 8, 3),
(948.5, STR_TO_DATE('10/09/2017', '%d/%m/%Y'), 5, 2),
(2400.6, STR_TO_DATE('27/07/2016', '%d/%m/%Y'), 7, 1),
(5760, STR_TO_DATE('10/09/2015', '%d/%m/%Y'), 2, 1),
(1983.43, STR_TO_DATE('10/10/2017', '%d/%m/%Y'), 4, 6),
(2480.4, STR_TO_DATE('10/10/2016', '%d/%m/%Y'), 8, 3),
(250.45, STR_TO_DATE('27/06/2015', '%d/%m/%Y'), 8, 2),
(75.29, STR_TO_DATE('17/08/2016', '%d/%m/%Y'), 3, 7),
(3045.6, STR_TO_DATE('25/04/2017', '%d/%m/%Y'), 2, 1),
(545.75, STR_TO_DATE('25/01/2019', '%d/%m/%Y'), 6, 1),
(145.82, STR_TO_DATE('02/02/2017', '%d/%m/%Y'), 6, 1),
(370.85, STR_TO_DATE('11/03/2019', '%d/%m/%Y'), 1, 5),
(2389.23, STR_TO_DATE('11/03/2019', '%d/%m/%Y'), 1, 5);

SELECT * FROM Pedidos p ORDER BY p.FECHA DESC;

SELECT * FROM Pedidos p
WHERE p.TOTAL BETWEEN 300 AND 600
ORDER BY p.FECHA ASC;

SELECT ID, NOMBRE , APELLIDO1 FROM Cliente
WHERE APELLIDO2 IS NULL
ORDER BY APELLIDO1 ASC, NOMBRE ASC;

SELECT DISTINCT c.ID, c.NOMBRE, c.APELLIDO1, c.APELLIDO2
FROM Cliente c
JOIN Pedidos p ON c.ID = p.ID_CLIENTE
ORDER BY c.NOMBRE COLLATE utf8mb4_unicode_ci ASC,
         c.APELLIDO1 COLLATE utf8mb4_unicode_ci ASC,
         c.APELLIDO2 COLLATE utf8mb4_unicode_ci ASC;

SELECT DISTINCT c.NOMBRE, c.APELLIDO1, c.APELLIDO2
FROM Comercial c
JOIN Pedidos p ON c.ID = p.ID_COMERCIAL
JOIN Cliente cl ON p.ID_CLIENTE = cl.ID
WHERE cl.NOMBRE = 'Mariá' 
  AND cl.APELLIDO1 = 'Santana' 
  AND cl.APELLIDO2 = 'Moreno';

-- DROP VIEW IF EXISTS `ResumenPedidos`;
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

-- SELECT * FROM ResumenPedidos;

SELECT 
    Comercial_Nombre, Comercial_Apellidos,
    SUM(Pedidos_Total) AS Total_Ventas, 
    AVG(Pedidos_Total) AS Promedio_Ventas, 
    COUNT(Pedido_ID) AS Cantidad_Pedidos
FROM ResumenPedidos
GROUP BY Comercial_Nombre, Comercial_Apellidos
ORDER BY Total_Ventas DESC;
