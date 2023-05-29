Algoritmo divisiblees
	// Definimos las variables como entero
	Definir num1,num2 Como Entero
	// Input para pedir el numero al usuario
	Escribir 'Digite un numero'
	// Se guarda en la variable num1
	Leer num1
	// Pedimos otro numero
	Escribir 'Digite otro numero'
	// Lo guardamos en otra variable num2
	Leer num2
	// preguntamos si el resultado de la division de numero1=num1 y numero2=num2 es cero
	si num1 mod num2 == 0 Entonces
		// Si es cero entoces son divisibles los numeros
		Escribir 'Son divisibles'
	SiNo
		// Caso contrario no son divisibles
		Escribir 'No son divisibles'
	FinSi
FinAlgoritmo
