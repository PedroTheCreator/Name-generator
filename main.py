from tkinter import *
import names
def tfb(app,texto,x,y,w,h):
  Label(app,text=texto,background="#dde", foreground="#009",anchor=W).place(x=x,y=y,width=w,h=20)
def button(app,texto,comando, x,y,w,h):
  btn = Button(app, text=texto,command=comando).place(x=x,y=y,width=w,h=20)
def dados():
  global menu 
  menu = int(form.get())
  print(menu)
app=Tk()
app.configure(background="#dde")
app.geometry("1280x720")
escolha = 2
counter = 0
nomes = []
counter2= 11
list_counter = 1
menu = "===== Gerador de nomes =====\nMenu:\n1 --> Nomes masculinos\n2 --> Nomes femininos"
tfb(app,"===== Gerador de nomes =====",10,10,250,20)
tfb(app,"Menu:",10,30,250,20)
tfb(app,"1 --> Nomes masculinos",10,50,250,20)
tfb(app,"2 --> Nomes femininos",10,70,250,20)
tfb(app,"Insira sua escolha",10,90,250,20)
menu = 0
form = Entry(app)
form.place(x=10,y=110, width=200,height=20)
button(app,"Enviar",dados,10,140,75,75)
print(menu)
#print("===== Gerador de nomes =====\nMenu:\n1 --> Nomes masculinos\n2 --> Nomes femininos")

if menu == 1: 
  genero = "male"
elif menu == 2:
  genero = "female"
else: 
    print("Opção inválida.")
try:
  #tfb(app,"Insira sua escolha",10,130,250,20)
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
print("Fim do programa.")        


app.mainloop()