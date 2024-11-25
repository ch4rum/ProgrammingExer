DELIMITER $$
DROP DATABASE IF EXISTS `ShopSt`;
CREATE DATABASE `ShopSt`;
USE `ShopSt`;

-- DROP TABLE IF EXISTS `Productos`;

CREATE TABLE IF NOT EXISTS `Productos`(
    `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `NOMBRE` VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    `PRECIO` DECIMAL(9,2) UNSIGNED NOT NULL,
    `STOCK` INT UNSIGNED NOT NULL,
    CONSTRAINT `product_id` PRIMARY KEY(`ID`)
)DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- DROP TABLE IF EXISTS `Registro_ventas`;

CREATE TABLE IF NOT EXISTS `Registro_ventas`(
    `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `ID_PRODUCTO` INT UNSIGNED NOT NULL,
    `CANTIDAD` INT UNSIGNED NOT NULL,
    `FECHA_VENTA` TIMESTAMP NOT NULL DEFAULT (NOW()),
    CONSTRAINT `sale_id` PRIMARY KEY(`ID`),
    CONSTRAINT `id_product_pk` FOREIGN KEY (`ID_PRODUCTO`) REFERENCES `Productos`(`ID`)
)DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE OR REPLACE PROCEDURE cal_total_ventas()
BEGIN
    DECLARE flags TINYINT DEFAULT 0;
    DECLARE precio DECIMAL(9, 2);
    DECLARE cantidad INT;
    DECLARE total_ventas DECIMAL(10, 2) DEFAULT 0;

    DECLARE c1 CURSOR FOR 
        SELECT p.PRECIO, rv.CANTIDAD
        FROM Registro_ventas rv
        INNER JOIN Productos p ON rv.ID_PRODUCTO = p.ID;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET flags = 1;

    OPEN c1;
    read_loop:LOOP
        FETCH c1 INTO precio, cantidad;
        IF flags = 1 THEN 
            LEAVE read_loop;
        END IF;
        -- SELECT CONCAT('Peocedimiento: PRECIO=', precio, ', CANTIDAD = ', cantidad) AS Debug;
        SET total_ventas = total_ventas + (precio * cantidad);
    END LOOP read_loop;
    CLOSE c1;

    SELECT total_ventas AS TOTAL_VENTAS;
END$$

CREATE OR REPLACE FUNCTION obtener_stock_producto(p_id_product INT)
RETURNS INT 
DETERMINISTIC
BEGIN 
    DECLARE stock_product INT;
    SELECT STOCK 
    INTO stock_product
    FROM Productos
    WHERE ID = p_id_product;
    RETURN stock_product;
END$$

CREATE OR REPLACE PROCEDURE actualizar_stock(
    IN p_id_producto INT,
    IN p_cantidad_vendidad INT
)
BEGIN
    UPDATE Productos
    SET STOCK = STOCK - p_cantidad_vendidad
    WHERE ID = p_id_producto;
    -- SELECT CONCAT('Stock actualizado') AS UPDATE_STOCK;
END$$

CREATE OR REPLACE TRIGGER  actualizar_stock_trg_insert
BEFORE INSERT ON Registro_ventas
FOR EACH ROW 
BEGIN
    CALL actualizar_stock(NEW.ID_PRODUCTO, NEW.CANTIDAD);
END$$

CREATE OR REPLACE TRIGGER  actualizar_stock_trg_update
BEFORE UPDATE ON Registro_ventas
FOR EACH ROW 
BEGIN
    CALL actualizar_stock(NEW.ID_PRODUCTO, NEW.CANTIDAD);
END$$

DELIMITER ;