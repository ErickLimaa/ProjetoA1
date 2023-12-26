def decimal_para_binario(decimal):
  return bin(decimal)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)
  
def adicao_binario(retorno_bin1, retorno_bin2):
  decimal1 = binario_para_decimal(retorno_bin1)
  decimal2 = binario_para_decimal(retorno_bin2)
  resultado = decimal1 + decimal2
  return decimal_para_binario(resultado)
  
def subtracao_binario(retorno_bin1, retorno_bin2):
  decimal1 = binario_para_decimal(retorno_bin1)
  decimal2 = binario_para_decimal(retorno_bin2)
  resultado = decimal1 - decimal2
  return decimal_para_binario(resultado)

def menu():
  print('''
    MENU:
    
    (Opção 1:) = Conversão para decimal para as bases binário e octadecimal. 
    (Opção 2:) = Conversão das bases binário e octadecimal para decimal.
    (Opção 3:) = Calculadora aritmética de binários, que contemple as operações de soma e subtração.
    (Opção 4:) = Sair do programa.
  ''')
  
def executar_programa():
  while True:
    menu()
    opcaoDesejada = input("Qual a função desejada? ")

    if opcaoDesejada == "1":
      decimal = int(input("Digite o número decimal:"))
      bina = bin(decimal)
      octa = oct(decimal)
      print("O valor em binário:", bina[2:])
      print("O valor em octadecimal:", octa[2:])
      exit()

    elif opcaoDesejada == "2":
      binario = input("Digite um número binário: ")
      deci = int(binario, 2)
      print("O valor em decimal: ", deci)
      octal = input("Digite o número octal: ")
      decimal = int(octal, 8)
      print("O valor em decimal", decimal)
      exit()

    elif opcaoDesejada == "3":
      binario1 = input("Digite o primeiro número binário: ")
      binario2 = input("Digite o segundo número binário: ")
      calculo = adicao_binario(binario1, binario2)
      calculo_subtracao = subtracao_binario(binario1, binario2)
      print("Resultado da adição",calculo)
      print("Resultado da subtração",calculo_subtracao )
      exit()
  
    elif opcaoDesejada == "4":
      print("Programa encerrado")
      break

    else:
      print("Opção inválida. Escolha uma opção válida: ")


executar_programa()

# Os desenvolvedores são:
# Erick Lima Prudencio da Silva - 33755698
# Guilherme Pereira Fagundes - 33597995
# Hiago Rocha de Melo - 34171959
# Campus Paulista

