import names
from colorama import Fore, init, Style
import os
init(autoreset=True)
escolha = 2
counter = 0 ; terminador = 1 
counter2= 11
counter3= 0
list_counter = 1
x = ""
nomes = [] ; salvos = []

#print(y)
#print(type(y))
#print(len(total_nomes))
#print(total_nomes)
#print(total)

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
        leitura = open("nome.txt","r")
        total_nomes = leitura.readline()
        total = int(total_nomes[23:(len(total_nomes))])
        arquivo = open("nome.txt","a+")
        if inicial != "-":
          nome=names.get_full_name(gender=genero)
          #print(nome[0:0])
          if nome[0:1] == inicial:
            counter+=1
            print(Fore.YELLOW + str(counter) + ". " + Fore.LIGHTYELLOW_EX + str(nome))
            nomes.append(nome)
        else:
          nome=names.get_full_name(gender=genero)
          counter+=1
          print(Fore.YELLOW + str(counter) + ". " + Fore.LIGHTYELLOW_EX + str(nome))
          nomes.append(nome)
        if counter == (counter2-1):
          escolha = str(input(Fore.GREEN + "Digite: "))
          list_counter+=1
          counter2= counter2 + 10 
          os.system('clear')
          if escolha != "1" and escolha.lower() != "save" and escolha.lower() != "salvar":
            print(Fore.GREEN + "\n===== Lista {} =====".format(list_counter))
            nomes.clear()
          elif escolha.lower() == "salvar" or escolha.lower() == "save":
            save = str(input("Salvar\n1 --> Salvar a lista\n2 --> Salvar um nome\nDigite: "))
            if save == "1":
              conteudo = leitura.read()
              arquivo.close()
              arquivo = open("nome.txt", "w")
              arquivo.close()
              arquivo = open("nome.txt", "a+")
              arquivo.write("Total de nomes salvos: " + str(total+10) + "\n")
              arquivo.write(conteudo)
              counter3=total
              for i in nomes:
                counter3+=1
                arquivo.write("\n" + str(counter3) + ". " + i)
              counter3=0
              os.system("clear")
              print("Lista salva")
              os.system("sleep 1")
              os.system("clear")
              arquivo.close()
              nomes.clear()
            elif save == "2":
              while(x.lower() != "sair"):
                os.system("clear")
                print(Fore.GREEN + "===== Lista analisada =====")
                for i in nomes:
                  counter3+=1
                  print("{}. {}".format( (Fore.YELLOW + str(counter3)), (Fore.LIGHTYELLOW_EX + str(i)) ))
                x = str(input(Fore.GREEN + "Insira qual nome deseja salvar: "))
                if x.lower() == "sair":
                  break
                else:
                  x = int(x)
                  #print("Tipo: {}\n Valor: {}".format(type(x), x))
                  y = nomes[(x-1)]
                  nomes.pop(x-1)
                  os.system("clear")
                  print("Nome que será salvo: " + y)
                  os.system("sleep 1")
                  salvos.append(y)
                  x = str(x)
                  counter3=0
              conteudo = leitura.read()
              arquivo.close()
              arquivo = open("nome.txt", "w")
              arquivo.close()
              arquivo = open("nome.txt", "a+")
              total_salvo = int(len(salvos))
              arquivo.write("Total de nomes salvos: " + str(total+total_salvo) + "\n")
              arquivo.write(conteudo)
              counter3=total
              for i in salvos:
                counter3+=1
                arquivo.write("\n" + str(counter3) + ". " + i)
              print("Nome salvo")
              arquivo.close()
              nomes.clear()
            else:
              print("Opção inválida, não foi possível salvar")
              nomes.clear()
          elif escolha == "1":
            break           
  except ZeroDivisionError:
    print(Fore.RED + "O programa não pode continuar.")
print(Fore.RED + "Fim do programa")    
os.system('sleep 5')
arquivo.close()
leitura.close()
os.system('clear')
