import tkinter as tk
from tkinter import ttk

menu = {
    'Pizza': 50.00,
    'Bauru': 5.50,
    'Coca-Cola': 3,
}

lista_pedidos = []
lista_quantidades = []


def confirmação(var_quantidade_1, var_pedido_1):
    pedido_final = ttk.Label(window, font = "Calibre 10 bold")
    pedido_final.config(text = f"Você adicionou {var_quantidade_1.get()} {var_pedido_1.get()}(s)")
    lista_pedidos.append(var_pedido_1.get())
    lista_quantidades.append(var_quantidade_1.get())
    pedido_final.pack()
    print(lista_pedidos)
    print(lista_quantidades)

def limpar(pedidos,pedidos_q):
    if len(lista_pedidos) < 1:
        pedido_final = ttk.Label(window, font = "Calibre 10 bold")
        pedido_final.config(text = f"Seu carrinho está vazio, faça algum pedido!")
        pedido_final.pack()
    else:
        pedido_final = ttk.Label(window, font = "Calibre 11 bold")
        lista_pedidos.pop()
        lista_quantidades.pop()
        pedido_final.config(text = f"Último pedido removido")
        pedido_final.pack()
    print(lista_pedidos)
    print(lista_quantidades)

def mostrar(lista_pedidos, lista_quantidades):
    mostrar_lista = ttk.Label(window, text = "Lista de Pedidos", font = 'Calibre 11 bold')
    mostrar_lista.config(text = f"Seus pedidos: {lista_pedidos} e \n as quantidades respectivamente {lista_quantidades}")
    mostrar_lista.pack()

def subtotal(lista_pedidos, lista_quantidades):
    total = 0 + total
    while len(lista_pedidos) >= 0:
        calc = (menu.get(lista_pedidos[0]) * int(lista_quantidades[0]))
        total = calc + total 
        lista_pedidos.pop(0)
        lista_quantidades.pop(0)
        print(lista_pedidos)
        print(lista_quantidades)
        subtotal(lista_pedidos,lista_quantidades)
    print(f"Total: R${total}")

#window
window = tk.Tk()
window.geometry("400x600")
window.title("Simulador de pedidos - Ifood")

#model
cardapio = ('Pizza','Bauru','Coca-Cola')
pedido_1 = ttk.Combobox(window)
var_pedido_1 = tk.StringVar()
pedido_1.configure(values = cardapio, textvariable = var_pedido_1)
pedido_1.pack()

var_quantidade_1 = tk.IntVar()
quantidade_1 = ttk.Spinbox(window, textvariable = var_quantidade_1, from_ = 1, to = 10)
quantidade_1.pack(pady = 5)

pedido_1_label = ttk.Label(window, font = "Roboto 12 italic")
pedido_1_label.pack()

#BIND DE EVENTO FUNCIONA COM .PACK() e USANDO CONFIG/CONFIGURE DÁ PRA ALTERAR STRING(TEXTO) 
pedido_1.bind('<<ComboboxSelected>>', lambda event: pedido_1_label.config(text = f"Você adicionou {var_quantidade_1.get()} {var_pedido_1.get()} ao carrinho"))

carrinho = ttk.Frame(master = window)
confirm = ttk.Button(window, text = "Confirmar", command = lambda: confirmação(var_quantidade_1,var_pedido_1))
confirm.pack(pady = 5)

limp = ttk.Button(window, text = "Limpar", command = lambda: limpar(lista_pedidos,lista_quantidades))
limp.pack(pady = 5)

mostrar_botão = ttk.Button(window, text = "Mostrar Pedidos", command = lambda: mostrar(lista_pedidos,lista_quantidades))
mostrar_botão.pack(pady = 5)

subtotal_botão = ttk.Button(window, text = "Subtotal", command = lambda: subtotal(lista_pedidos,lista_quantidades))
subtotal_botão.pack(pady = 5)

#run
window.mainloop()