Algoritmo plus_less_zero
	// Pedir al usuario que digite un numero
	Escribir 'Digite un numero'
	// Guardar un numero en la variable num1
	Leer num1
	// Preguntamos si el numero es igual a cero
	Si num1 = 0 Entonces
		// Output Cero
		Escribir 'El numero es cero'
	SiNo
		// Preguntamos si es mayor q cero para saber si es positivo, caso contrario Negativo
		Si num1 > 0 Entonces
			// Output Positivo
			Escribir 'El numero ',num1, ' es Positivo'
		SiNo
			// Output Negativo
			Escribir 'El numero ',num1, ' es Negativo'
		FinSi
	FinSi
FinAlgoritmo
