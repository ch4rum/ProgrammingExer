// Algoritmo tienda de dulces 
Funcion iva_product ( amount, price )
	// Funcion que pide cantidad y precio
	// Con impuesto de 5% = 0.05 y si la cantidad del producto a comprar es mayor a 5
	// se le hace un descuento de 3% = 0.03 sobre lo que va ha pagar el usuario
	values_un = amount * price
	iva = values_un * 0.05
	total = values_un + iva
	Si amount > 5 Entonces
		iva = total * 0.03
		total = total - iva
		Escribir 'Total a pagar es $',total
	SiNo
		Escribir 'Total a pagar es $',total
	FinSi
Fin Funcion

Algoritmo Welcome_to_the_candy_store
	// Definimos las variables de selecion y cantidad como entero
	Definir selection, amount  Como Entero
	// Hacemos un pequeño menu motrandole al usuario varias opciones
	Escribir 'Welcome to the candy store'
	Escribir '1- Maíz : 1500'
	Escribir '2- Chocolate: 2000'
	Escribir '3- Galletas: 800'
	Escribir '4- Masmelos: 500'
	// Guardamos en selection la opcion del usuario
	Leer selection
	// Opciones del menu
	Segun selection Hacer
		1:
			// Si la selecion es 1 muestra al usuario producto seleccionado y le pide la cantidad que desea comprar
			Escribir 'Producto Maiz'
			Escribir 'Ingrese la cantidad del producto'
			Leer amount
			// Se llama la funcion y se le pasa la cantidad y el precio del producto Selecionado
			iva_product(amount, 1500)
		2:
			// Si la selecion es 2 muestra al usuario producto seleccionado y le pide la cantidad que desea comprar
			Escribir 'Producto Chocolate'
			Escribir 'Ingrese la cantidad del producto'
			Leer amount
			// Se llama la funcion y se le pasa la cantidad y el precio del producto Selecionado
			iva_product(amount, 2000)
		3:
			// Si la selecion es 3 muestra al usuario producto seleccionado y le pide la cantidad que desea comprar
			Escribir 'Producto Galletas'
			Escribir 'Ingrese la cantidad del producto'
			Leer amount
			// Se llama la funcion y se le pasa la cantidad y el precio del producto Selecionado
			iva_product(amount, 800)
		4:
			// Si la selecion es 4 muestra al usuario producto seleccionado y le pide la cantidad que desea comprar
			Escribir 'Producto Masmelos'
			Escribir 'Ingrese la cantidad del producto'
			Leer amount
			// Se llama la funcion y se le pasa la cantidad y el precio del producto Selecionado
			iva_product(amount, 500)
		De Otro Modo:
			// Si la selecion del usuario noes 1 2 3 o 4 se le muestra que no selecciono algun producto
			Escribir 'No seleciono algun producto'
	Fin Segun
	
FinAlgoritmo
