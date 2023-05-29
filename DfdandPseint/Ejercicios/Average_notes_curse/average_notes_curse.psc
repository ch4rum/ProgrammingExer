Funcion average <- notesAverage ( )
	// Funcion que pide las notas y se repite si las notas no van de 1 a 10 
	// Luego saca el promedio de las 3 notas y retorna el resultado
	Repetir
		Escribir 'Dame primera nota'
		Leer note1
	Hasta Que note1>1 Y note1<=10
	Repetir
		Escribir 'Dame segunda nota'
		Leer note2
	Hasta Que note2>1 Y note2<=10
	Repetir
		Escribir 'Dame tercera nota'
		Leer note3
	Hasta Que note3>1 Y note3<=10
	average = (note1+note2+note3)/3
Fin Funcion

Algoritmo average_notes_curse
	// Definimos una variables como real y la otras como string
	Definir note1,note2,note3,average,numberStudent,averageStudent Como Real
	Definir student,name Como Caracter
	// Decimos que si desea agregar un estudiante
	Escribir 'Desea Ingresar un Estudiante S/N'
	// guardamos ese resultado en la variable student
	Leer student
	// las variables estan en cero por default
	numberStudent = 0
	averageStudent = 0
	// Mientras la variable student sea diferente de N se ejecuta el codigo
	Mientras student <> 'N' Hacer
		// Si agrega un estudiante le suma 1 para ir contandolos
		numberStudent = numberStudent + 1
		// Preguntamos el nombre del estudiante y lo guardamos en una variable name
		Escribir 'Nombre estudiante'
		Leer name
		// Guardamo el retorno de la funcion en la variable average y se llama la Funcion 
		average = notesAverage()
		// Le sumamos el promedio a la variable de promedioestudiantes
		averageStudent = averageStudent + average
		// Mostramos el promedio del estudiante ingresado
		Escribir 'El promedio de ',name,' es: ',average
		// Preguntamos si desea agregar otro estudiante y guardamos el resultado en la misma varible student
		Escribir 'Desea Ingresar un Estudiante S/N'
		Leer student
	Fin Mientras
	// Si el numero estudiante es diferente a cero significa que si saco o notas para los estudiantes
	Si numberStudent <> 0 Entonces
		// Sacamos el promedio del curso en la misma variable promedioEstudiantes 
		averageStudent = averageStudent/numberStudent
		// Mostramos el promedio del curso y el numero de estudiantes
		Escribir 'Numero de estudiantes: ',numberStudent,', promedio del curso: ',averageStudent
	SiNo
		// Sino es diferente de 0significa que no saco notas de los estudiantes, mostramos que no ingreso estudiantes
		Escribir 'No ha ingresado estudiantes' 
	Fin Si
	
FinAlgoritmo
