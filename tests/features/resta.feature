Feature: Resta de dos numeros
	como usuario de la calculadora
	deseo realizar la resta de dos numeros 
	para obtener el resultado preciso

	Scenario: Resta de 5 menos 3
		Dado que resto los numeros "5" y "3"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Resta de 7 menos 10
		Dado que resto los numeros "7" y "10"
		cuando realizo la operación
		entonces obtengo el resultado "-3"

	Scenario: Resta de 8 menos -7
		Dado que resto los numeros "8" y "7"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Resta de 0 menos 7 
		Dado que resto los numeros "0" y "-7"
		cuando realizo la operación
		entonces obtengo el resultado "7"