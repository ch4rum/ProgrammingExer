Algoritmo age_people
	// Definimos la variable edad como entero
	definir age Como Entero
	// Preguntamos al usuario cual es la edad que tiene 
	Escribir 'Cual es tu edad?'
	// Guardamos la edad en la variable age
	Leer age
	// Preguntamos si el usuario es mayor o igual a 1 y menor o igual a 18
	Si age >= 1 Y age <= 18 Entonces
		// Preguntamos si es menor o igual a 8
		Si age <= 8 Entonces
			// Output primera infancia
			Escribir 'Primera Infancia'
		FinSi
		// Preguntmaos si es mayor o igual a 9 y menor o igual a 12
		Si age >= 9 Y age <= 12 Entonces
			// Output segunda infancia
			Escribir 'Segunda infancia'
		FinSi
		// Preguntamos si es mayor o igual a 13 y menor o igual a 15
		Si age >= 13 Y age <= 15 Entonces
			// Output pre adolecente
			Escribir 'Pre adolescente'
		FinSi
		// Preguntmaos si es mayor o igual a 16 y menor o igual a 18
		Si age >= 16 Y age <= 18 Entonces
			// Output adolecente
			Escribir 'Adolescente'
		FinSi
	SiNo
		// Si es mayor a 18, Output mayor de edad
		Escribir 'Es mayor de edad'
	Fin Si
	
FinAlgoritmo
