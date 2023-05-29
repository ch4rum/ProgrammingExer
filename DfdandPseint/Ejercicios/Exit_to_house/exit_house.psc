Algoritmo exit_house
	// Se prengunta al usuario si esta fuera de la casa  S = si, N = no
	Escribir 'Estas fuera de la casa? S/N'
	// Se guarda la respuesta del usuario en la variable casa'
	Leer casa
	Si casa='S' Entonces
		// Si  el usuario responde S = si 
		// Se le pregunta si quiere entrar a la casa 
		Escribir 'Quieres entrar a la casa? S/N'
		// Se procede a guardar la  respuesta en la variable entrar
		Leer entrar
		Si entrar='S' Entonces
			// Si entra a la casa pues tendra que abrirla
			Escribir 'Abrir la puerta de la casa'
		SiNo
			// Sino entra significa que esta por fuera aun
			Escribir 'Estas fuera de la casa'
		FinSi
	SiNo
		// Si el usuario respondio que N= no
		Repetir
			// Se le pregunta si tiene llaves para salir de la casa y no quedarse por fuera
			Escribir 'Tienes llaves? S/N'
			// Se guarda la respuesta en la variable llaves
			Leer llaves
			Si llaves='N' Entonces
				// Si el usuario no tiene llaves tendra que buscarlas hasta encontrarlas
				Escribir 'busca las llaves'
			FinSi
		Hasta Que llaves='S'
		Repetir
			// Se le pregunta si tiene el bolso donde lleva sus cosas
			Escribir 'Tienes bolso? S/N'
			// se procede ha guardar la respuesta en la variable bolso
			Leer bolso
			Si bolso='N' Entonces
				// Sino tiene bolso lo busca hasta encontrarlo
				Escribir 'burcar bolso'
			FinSi
		Hasta Que bolso='S'
		// Se le pregunta si necesiat llevar lago mas
		Escribir 'Necesitas algo mas? S/N'
		// Se guarda la respuesta en la variable algoMas
		Leer algoMas
		Si algoMas='S' Entonces
			// Si dice que nesesita lago le decimos que lo busque
			Escribir 'Buscar lo que necesito'
		FinSi
		// sale de la casa
		Escribir 'Salir de la casa'
	FinSi
FinAlgoritmo
