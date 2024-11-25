USE `ShopSt`

INSERT INTO `Productos` (NOMBRE, PRECIO, STOCK)
VALUES
('Producto A', 50, 100),
('Producto B', 75, 80),
('Producto C', 60, 120),
('Producto D', 90, 60);

INSERT INTO `Registro_ventas`(ID_PRODUCTO, CANTIDAD)
VALUES
(1, 15);

SELECT * FROM `Productos`;

SELECT * FROM `Registro_ventas`;

SELECT p.PRECIO, rv.CANTIDAD
FROM `Registro_ventas` rv
INNER JOIN `Productos` p ON rv.`ID_PRODUCTO` = p.ID;

CALL cal_total_ventas();

SELECT obtener_stock_producto(3) AS STOCK;

CALL actualizar_stock(3, 20);

SHOW TRIGGERS LIKE 'Registro_ventas';

UPDATE `Registro_ventas`
SET `CANTIDAD` = 10
WHERE `ID_PRODUCTO`= 1;