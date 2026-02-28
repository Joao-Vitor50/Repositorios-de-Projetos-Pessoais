def Calculadora():
	import time
	
	print("Iniciando Calculadora...")
	time.sleep(2)
	print("Calculadora iniciada!!")
	while True:
		try:
			Primeiro_valor = int(input("Digite o primeiro valor: "))
			Segundo_valor = int(input("Digite o segundo valor: "))
			sinal = input("Digite o sinal correspondente (soma, subtração, multiplicação ou divisão): ").lower()

			if sinal not in ["soma", "subtração", "multiplicação", "divisão"]:
				print("Sinal inválido, tente novamente.")
				continue

		except ValueError:
			print("Valor incompatível, tente novamente.")
			continue

		# Operações
		if sinal == "soma":
			resultado = Primeiro_valor + Segundo_valor
			print(f"O resultado de {Primeiro_valor} + {Segundo_valor} é {resultado}")

		elif sinal == "subtração":
			resultado = Primeiro_valor - Segundo_valor
			print(f"O resultado de {Primeiro_valor} - {Segundo_valor} é {resultado}")

		elif sinal == "multiplicação":
			resultado = Primeiro_valor * Segundo_valor
			print(f"O resultado de {Primeiro_valor} * {Segundo_valor} é {resultado}")

		elif sinal == "divisão":
			if Segundo_valor == 0:
				print("Não é possível dividir por zero.")
				continue

			resultado = Primeiro_valor / Segundo_valor
			print(f"O resultado de {Primeiro_valor} / {Segundo_valor} é {resultado}")

		# Saída
		while True:
			saida_Calculadora = input("Deseja fazer outro cálculo? (S/N): ").upper().strip()

			if saida_Calculadora == "N":
				print("Saindo do aplicativo...")
				time.sleep(2)
				print("Aplicativo finalizado.")
				return

			elif saida_Calculadora == "S":
				break

			else:
				print("Opção incorreta, tente novamente.")


Calculadora()


#LISTA DE COISAS APRENDIDAS
"Try e except"
"Debug com print de um input pra ver se oque está sendo digitado está certo"
".upper() e .string() pra forçar informações de variaveis a terem certos parametros"
"ValueError"
