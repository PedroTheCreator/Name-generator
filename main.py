import names
from colorama import Fore, init, Style
import os
init(autoreset=True)
escolha = 2
counter = 0 ; terminador = 1 
counter2= 11
list_counter = 1
print(Fore.CYAN + "===== Gerador de nomes ====="+ Fore.RESET + "\nMenu:" + Fore.LIGHTMAGENTA_EX + "\n1 --> Nomes masculinos" + Fore.BLUE + "\n2 --> Nomes femininos")
menu = int(input(Fore.CYAN + Style.BRIGHT + "Insira sua escolha: "))
if menu == 1: 
  genero = "male"
elif menu == 2:
  genero = "female"
else: 
  print(Fore.RED + "Opção inválida.")
  terminador = 0
os.system('clear')
if terminador != 0:
  print(Style.RESET_ALL + Fore.YELLOW + "\nGostaria de escolher a inicial?"+ Fore.WHITE +"\n1 --> Sim\n2 --> Não")
  menu = int(input(Fore.YELLOW + "Insira sua escolha: "))
  if menu == 1: 
    inicial = str(input("Insira a inicial: ")).title()
    terminador=1
  elif menu == 2:
    print(Fore.LIGHTYELLOW_EX + "Nomes completamente aleatórios serão gerados!\n")
    terminador=1
    inicial = "-"
  else: 
    terminador = 0
    print(Fore.RED + "Opção inválida.")
os.system('sleep 2')
os.system('clear')
if terminador == 1:
  try:
    print(Fore.GREEN + "\n===== Lista {} =====".format(list_counter))
    while(escolha != 1 and counter < counter2):
        if inicial != "-":
          nome=names.get_full_name(gender=genero)
          #print(nome[0:0])
          if nome[0:1] == inicial:
            counter+=1
            print(Fore.YELLOW + str(counter) + ". " + Fore.LIGHTYELLOW_EX + str(nome))
        else:
          nome=names.get_full_name(gender=genero)
          counter+=1
          print(Fore.YELLOW + str(counter) + ". " + Fore.LIGHTYELLOW_EX + str(nome))
        if counter == (counter2-1):
          escolha = int(input(Fore.GREEN + "Digite: "))
          list_counter+=1
          counter2= counter2 + 10 
          os.system('clear')
          if escolha != 1:
            print(Fore.GREEN + "\n===== Lista {} =====".format(list_counter))
  except:
    print(Fore.RED + "O programa não pode continuar.")
print(Fore.RED + "Fim do programa")    
os.system('sleep 5')
os.system('clear')