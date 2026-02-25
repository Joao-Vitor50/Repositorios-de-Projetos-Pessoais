#Perguntas para escolher os numeros e o sinal
 Primeiro_valor = int(input("Digite o primeiro valor: "))
 Segundo_valor = int(input("Digite o primeiro valor: "))
 sinal = input("Digite o sinal correspondente( soma, subtração, mutiplicação ou divisão): ")
 if Primeiro_valor or Segundo_valor == "" or sinal != "soma" or "mutiplicação" or "subtração" or "divisão":
 print("valor ou sinal imcompativél, Porfavor, tente denovo")

#Condições
if sinal == "soma":
 resultado = Primeiro_valor + Segundo_valor
 print(f"o resultado de {Primeiro_valor} somado {Segundo_valor} é {resultado}")
 
elif sinal == "subtração":
 resultado = Primeiro_valor - Segundo_valor
 print(f"o resultado de {Primeiro_valor} subtraido{Segundo_valor} é {int(resultado)}")
elif sinal == "mutiplicação":
 resultado = Primeiro_valor * Segundo_valor
 print(f"o resultado de {Primeiro_valor} vezes {Segundo_valor} é {int(resultado)}")
elif sinal == "divisão":
 resultado = Primeiro_valor / Segundo_valor 
 print(f"o resultado de {Primeiro_valor} dividido por {Segundo_valor} é {int(resultado)}")
elif sinal != "soma" or "subtração" or "mutiplicação" or "divisão":
 print("valor incompativél")
