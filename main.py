#Sorveteria delivery

#Importando as bibliotecas necessarias
import tkinter as tk
from tkinter import *

#Criando a janela principal
janela = tk.Tk()
janela.title('Sorveteria do Cascão')

#Criando a lista de sabores
sabores = ['Chocolate','Morango','Limão','Banana','Kiwi','Flocos','Menta','Melancia']

#Criando a função que retorna a estimativa do tempo de entrega
def estimativa(sala):
    #Estimativa de entrega
    if sala <= 150:
        return "20 minutos"
    elif sala > 150 and sala <= 300:
        return "30 minutos"
    else:
        return "40 minutos"

#Criando a função que exibe a janela de finalização do pedido
def finalizar_pedido():
    #Recebendo os dados do pedido
    sala = int(sala_entry.get())
    sabor = sabor_escolhido.get()

    #Criando a janela de finalização
    janela_finalizacao = tk.Toplevel()
    janela_finalizacao.title('Finalizar Pedido')
    
    #Criando o frame
    frame_finalizacao = tk.Frame(janela_finalizacao)
    frame_finalizacao.pack()

    #Exibindo os dados do pedido
    Label(frame_finalizacao, text="Pedido Finalizado com Sucesso!").pack()
    Label(frame_finalizacao, text="Sabor Escolhido: {}".format(sabor)).pack()
    Label(frame_finalizacao, text="Sala: {}".format(sala)).pack()
    Label(frame_finalizacao, text="Estimativa de Entrega: {}".format(estimativa(sala))).pack()
    Label(frame_finalizacao, text="Nome do Cliente: {}".format(nome_cliente_entry.get())).pack()

#Criando o frame
frame = tk.Frame(janela)
frame.pack()

#Exibindo os sabores
Label(frame, text="Escolha o sabor:").pack()
sabor_escolhido = tk.StringVar(janela)
sabor_escolhido.set(sabores[0])
OptionMenu(frame, sabor_escolhido, *sabores).pack()

#Recebendo a sala
Label(frame, text="Digite a sala:").pack()
sala_entry = Entry(frame)
sala_entry.pack()

#Adicionando campo para inserção do nome do cliente
Label(frame, text="Digite seu nome:").pack()
nome_cliente_entry = Entry(frame)
nome_cliente_entry.pack()

#Criando o botão de finalizar pedido
Button(frame, text="Finalizar Pedido", command = finalizar_pedido).pack()

#Executando a janela principal
janela.mainloop()
