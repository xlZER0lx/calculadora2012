Feature: multiplicacion de dos numeros
	como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros 
	para obtener el resultado preciso

	Scenario: Multiplicacion de 5 por 3
		Dado que multiplico los numeros "5" y "3"
		cuando realizo la operación
		entonces obtengo el resultado "15"

	Scenario: Multiplicacion de 7 por 10
		Dado que multiplico los numeros "7" y "10"
		cuando realizo la operación
		entonces obtengo el resultado "70"

	Scenario: Multiplicacion de 8 por -7
		Dado que multiplico los numeros "8" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "-56"

	Scenario: Multiplicacion de 0 por 7 
		Dado que multiplico los numeros "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "0"