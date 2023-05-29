Algoritmo triangles
	// Definimos como real las variables
	Definir lado1, lado2, lado3 Como Real
	// Le pedimos al usuario los 3 lados del triangulo
	Escribir 'Ingrese los 3 lados del triangulo'
	// Se guardan los datos en las variables lado1 2 3
	Leer lado1, lado2, lado3
	// Equilatero 3 lados iguales
	// Comprobamos si los 3 lados son iguales
	si lado1 == lado2 Y lado1 == lado3 Y lado2 == lado3 Entonces
		// Output Equilatero
	  	Escribir 'Es Equilatero'
	FinSi
	// Isoceles 2 lados iguales
	// Preguntamos si dos de los lados son iguales y uno diferente
	si (lado1 == lado2 Y lado1 <> lado3) o (lado1 == lado3 Y lado1 <> lado2) o (lado2 == lado3 Y lado2 <> lado1) Entonces
		// Output Isoceles
		Escribir 'Es Isoceles'
	FinSi
	// Escaleno todos sus lados son diferentes
	// Preguntamos si todos los lados son diferentes
	Si lado1 <> lado2 Y lado1 <> lado3 Y lado2 <> lado3 Entonces
		// Output Escaleno
		Escribir 'Es Escaleno'
	FinSi
FinAlgoritmo
