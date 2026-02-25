#Fazendo o famoso Projeto Frankeistain
#Calculadora basica

#Perguntas para escolher os numeros e o sinal.
while True:
 while True:
  Primeiro_valor = input("Digite o primeiro valor: ")
  Segundo_valor = input("Digite o primeiro valor: ")
  sinal = input("Digite o sinal correspondente (soma, subtração, mutiplicação ou divisão): ")

  try: #Verificar se os valores estão corretamente digitados.(try e except foram comandos novos que aprendi no dia 2)
   Primeiro_valor = int(Primeiro_valor)
   Segundo_valor = int(Segundo_valor)
   sinal == ["soma", "subtração", "mutiplicação", "divisão"]
  except: #caso um desses valores estejam errados, o comando abaixo irar rodar.
   print("valor ou sinal imcompativél, Porfavor, tente denovo")
   continue
  else:
   break

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

 while True:#isso ainda não funciona por algum motivo
  SAIDA = input("Deseja fazer outro calculo?(S/N): ")#uma opção de saida que apareçera para o usuario depois de ter feito o calculo 
  if SAIDA == "S":
   continue
  elif SAIDA == "N":
   print("Saindo do Aplicativo...")
   print("Aplicativo finalizado")
   break
  else:
   print("Opção invalida")
   continue


#LISTA DE IDEIAS
#Fazer uma simulação de sistemas operacionais, ou sejá, um programa que me permite navegar e acessar aplicativos dentro dele mesmo, como essa calculadora.
