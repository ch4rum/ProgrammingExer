Algoritmo three_numbers
	// Definimos las 3 variables a pedir
	Definir num1, num2, num3 Como Entero
	// Pedimos que nos de 3 numeros
	Escribir 'Dame tres numeros'
	// Los numeros dados anteriormente los guardamo en las variables num1,num2 y num3
	Leer num1,num2,num3
	// Preguntamos si numero 1 es menor q el 2 y el 3
	Si num1 < num2 Y num1 <num3  Entonces
		// Para confirmar peguntamos si el numero 2 es menor que el 3
		Si num2 < num3 Entonces
			// Ya sabiendo q el numero 1 es menor y el numero 2 tambien
			// mostramos el output en orden 1 2 3
			Escribir 'Orden: ',num1,', ',num2,', ',num3
		SiNo
			// Caso contrario de  que el numero3 sea el menor
			// mostramos el Output en orden 1 3 2
			Escribir 'Orden: ',num1,', ',num3,', ',num2
		FinSi
	SiNo
		// Caso contario de que el uno no es el menor preguntamos si el numero 2 es el menor q numero 1 y numero 3
		Si num2 < num1 Y num2 < num3 Entonces
			// Preguntamos si numero 1 es menor que el numero 3
			Si num1 < num3 Entonces
				// Si es menor mostramos el Output en orden 2 1 3 
				Escribir 'Orden: ',num2,', ',num1,', ',num3
			SiNo
				// Si el numero 1 no es menor que el 3 mostramos Output en orden 2 3 1
				Escribir 'Orden: ',num2,', ',num3,', ',num1
			FinSi
		SiNo
			// Como numero 2 no es el menor preguntamos si numero 3 es menor que numero 1 y numero 2
			Si num3 < num1 Y num3 < num2 Entonces
				//  Preguntamos si numero 2 es menor que numero 1
				Si num2 < num1 Entonces
					// Si es menor mostramos el Output en orden 3 2 1 
					Escribir 'Orden: ',num3,', ',num2,', ',num1
				SiNo
					// Caso contrario que no sea el menor mostramos el Output en orden 3 1 2 
					Escribir 'Orden: ',num3,', ',num1,', ',num2
				FinSi
			FinSi
		FinSi
	Fin Si
	
FinAlgoritmo
