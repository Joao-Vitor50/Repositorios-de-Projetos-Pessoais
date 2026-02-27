#Fazendo o famoso Projeto Frankeistain - DIA 3
#Calculadora basica

#Perguntas para escolher os numeros e o sinal.
while True:
 try:
   Primeiro_valor = int(input("Digite o primeiro valor: "))
   Segundo_valor = int(input("Digite o Segundo valor: "))
   sinal = input("Digite o sinal correspondente (soma, subtração, mutiplicação ou divisão): ").upper()
  
   if sinal not in ["soma", "subtração", "mutiplicação", "divisão"]:
    print("Sinal invalido, tente novamente")
    continue
   
 except ValueError: #caso um desses valores estejam errados, o comando abaixo irar rodar.
   print("valor imcompativél, tente novamente")
   continue
 

 #Condições#_______________________________________________________________________________________________#
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
  if Segundo_valor == 0:
   print("Não é possivél dividir por zero")
   continue
  
  resultado = Primeiro_valor / Segundo_valor 
  print(f"o resultado de {Primeiro_valor} dividido por {Segundo_valor} é {int(resultado)}")
#_________________________________________________________________________________________________

 saida = input("Deseja fazer outro calculo?(S/N):").upper().strip() #uma opção de saida que apareçera para o usuario depois de ter feito o calculo 
  
 if saida == "N":
  print("Saindo do Aplicativo...")
  print("Aplicativo finalizado")
  break
  


#LISTA DE IDEIAS
#Fazer uma simulação de sistemas operacionais, ou sejá, um programa que me permite navegar e acessar aplicativos dentro dele mesmo, como essa calculadora.

#LISTA DE COISAS APRENDIDAS
"Try e except"
"Debug com print de um input pra ver se oque está sendo digitado está certo"
".upper() e .string() pra forçar informações de variaveis a terem certos parametros"
"ValueError"
