#import o tkinter para desenvolver a interface
from tkinter import *
from tkinter import ttk
from turtle import width
from unittest import result 

#definindo cores
cor1 = "#3b3b3b" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = '#FFAB40' #laranja

#criando janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg= cor1)

#criando frames e dividindo a janela
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variável todos_valores
todos_valores = ''

#criando label
val_texto = StringVar()

#criando função entrar_val
def entrar_val(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    #passando valor para a tela
    val_texto.set(todos_valores)

#função para calcular
def calc():
    global todos_valores
    result = eval(todos_valores)
    val_texto.set(str(result))
    todos_valores = str(result)

#função limpar tela: limpa no "C"
def limpar_tela():
    global todos_valores
    todos_valores = ""
    val_texto.set("")

app_label = Label(frame_tela, textvariable=val_texto, width=16, height=2, padx=7, relief=FLAT, anchor= "e", justify=RIGHT, fg= cor2,font=('Ivy 18'), bg= cor3)
app_label.place(x=0, y=0)

# criando botões

# a divisão dos botões está feita em fileiras
# a divisão começa da parte superior e a ordem é definida da esquerda para a direita

# fileira 1
b_1 = Button(frame_corpo, command=limpar_tela, text= "C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de clean "C" fundo: cinza, simb: preto
b_1.place(x=0, y=5)
b_2 = Button(frame_corpo, command= lambda: entrar_val('%'), text= "%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_2.place(x=118, y=5)
b_3 = Button(frame_corpo, command= lambda: entrar_val('/'), text= "/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de divisão "/" fundo: laranja,simb: branca
b_3.place(x=177, y=5)

#fileira2
b_4 = Button(frame_corpo, command= lambda: entrar_val('7'), text= "7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_4.place(x=0, y=60)
b_5 = Button(frame_corpo, command= lambda: entrar_val('8'), text= "8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_5.place(x=59, y=60)
b_6 = Button(frame_corpo, command= lambda: entrar_val('9'), text= "9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_6.place(x=118, y=60)
b_7 = Button(frame_corpo, command= lambda: entrar_val('*'), text= "*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de divisão "/" fundo: laranja,simb: branca
b_7.place(x=177, y=60)

#fileira3
b_8 = Button(frame_corpo, command= lambda: entrar_val('4'), text= "4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_8.place(x=0, y=110)
b_9 = Button(frame_corpo, command= lambda: entrar_val('5'), text= "5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_9.place(x=59, y=110)
b_10 = Button(frame_corpo, command= lambda: entrar_val('6'), text= "6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_10.place(x=118, y=110)
b_11 = Button(frame_corpo, command= lambda: entrar_val('-'), text= "-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de divisão "/" fundo: laranja,simb: branca
b_11.place(x=177, y=110)

#fileira4
b_12 = Button(frame_corpo, command= lambda: entrar_val('1'), text= "1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_12.place(x=0, y=160)
b_13 = Button(frame_corpo, command= lambda: entrar_val('2'), text= "2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_13.place(x=59, y=160)
b_14 = Button(frame_corpo, command= lambda: entrar_val('3'), text= "3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_14.place(x=118, y=160)
b_15 = Button(frame_corpo, command= lambda: entrar_val('+'), text= "+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de divisão "/" fundo: laranja,simb: branca
b_15.place(x=177, y=160)

#fileira5 
b_16 = Button(frame_corpo, command= lambda: entrar_val('0'), text= "0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de clean "C" fundo: cinza, simb: preto
b_16.place(x=0, y=215)
b_17 = Button(frame_corpo, command= lambda: entrar_val('.'), text= ".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de resto de divisão "%" fundo: cinza, simb: preto
b_17.place(x=118, y=215)
b_18 = Button(frame_corpo, command= calc, text= "=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #botão de divisão "/" fundo: laranja,simb: branca
b_18.place(x=177, y=215)

#chamando a aplicação
janela.mainloop()