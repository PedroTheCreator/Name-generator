import names
escolha = 2
counter = 0
nomes = []
counter2= 11
list_counter = 1
print("===== Gerador de nomes =====\nMenu:\n1 --> Nomes masculinos\n2 --> Nomes femininos")
menu = int(input("Insira sua escolha: "))
if menu == 1: 
  genero = "male"
elif menu == 2:
  genero = "female"
else: 
    print("Opção inválida.")
try:
  print("===== Lista {} =====".format(list_counter))
  while(escolha != 1 and counter < counter2):
      nome=names.get_full_name(gender=genero)
      counter+=1
      print("{}. {}".format(counter+1,nome))
      nomes.append(nome)
      if counter == (counter2-1):
          escolha = int(input(""))
          counter2= counter2 + 10 
except:
  print("O programa não pode continuar.")
print("Fim do programa")
            
             