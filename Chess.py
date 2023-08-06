import os
import msvcrt
import matplotlib.pyplot as plt

FichasBlancas=0
FichasNegras=0
NumeroMovimiento=0
YBlanca=[]
YNegra=[]
XMov=[]
def contar_ficha(tableros, ficha):
    contador=0
    for fila in tableros:
        contador+=fila.count(ficha)
    return contador
def esperar_tecla():
    print("Presiona una tecla para continuar...")
    msvcrt.getch()

# Función para imprimir el tablero
def imprimir_tablero(tableros):
    os.system("cls")
    for fila in tableros:
        print(" ".join(fila))
    print()

archivo=open("Movimientos.txt","r")
movimientos= archivo.read().splitlines()
tablero = [
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
    ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
    ["◻","◼","◻","◼","◻","◼","◻","◼"],
    ["◼","◻","◼","◻","◼","◻","◼","◻"],
    ["◻","◼","◻","◼","◻","◼","◻","◼"],
    ["◼","◻","◼","◻","◼","◻","◼","◻"],
    ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
]
filas=len(tablero)
columnas=len(tablero[0])
# Iterar a través de los movimientos y mostrar en el tablero
for movimiento in movimientos:
    imprimir_tablero(tablero)
    origen, destino = movimiento.split()
    fila_origen, columna_origen = int(origen[1]) - 1, ord(origen[0]) - ord("a")
    fila_destino, columna_destino = int(destino[1]) - 1, ord(destino[0]) - ord("a")
    tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
    tablero[fila_origen][columna_origen] = " "
    FichasBlancas=contar_ficha(tablero,"♙")+contar_ficha(tablero,"♖")+contar_ficha(tablero,"♘")+contar_ficha(tablero,"♗")+contar_ficha(tablero, "♔")+contar_ficha(tablero,"♕")
    FichasNegras=contar_ficha(tablero,"♟")+contar_ficha(tablero,"♜")+contar_ficha(tablero,"♞")+contar_ficha(tablero,"♝")+contar_ficha(tablero, "♚")+contar_ficha(tablero,"♛")
    NumeroMovimiento=NumeroMovimiento+1
    YBlanca.append(FichasBlancas)
    YNegra.append(FichasNegras+15)
    XMov.append(NumeroMovimiento/2)
    if tablero[fila_origen][columna_origen]==" ":
        if fila_origen==0 and columna_origen % 2 !=0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==0 and columna_origen % 2 ==0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==1 and columna_origen % 2 == 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==1 and columna_origen % 2 !=0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==2 and columna_origen % 2 != 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==2 and columna_origen % 2 ==0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==3 and columna_origen % 2 == 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==3 and columna_origen % 2 !=0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==4 and columna_origen % 2 != 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==4 and columna_origen % 2 ==0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==5 and columna_origen % 2 == 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==5 and columna_origen % 2 !=0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==6 and columna_origen % 2 != 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==6 and columna_origen % 2 ==0:
            tablero[fila_origen][columna_origen]="◻"
        elif fila_origen==7 and columna_origen % 2 == 0:
            tablero[fila_origen][columna_origen]="◼"
        elif fila_origen==7 and columna_origen % 2 !=0:
            tablero[fila_origen][columna_origen]="◻"
    esperar_tecla()
plt.plot(XMov,YBlanca, label='Blancas')
plt.plot(XMov,YNegra, label='Negras')
plt.fill_between(XMov,YBlanca, color="blue",alpha=0.2)
plt.fill_between(XMov,YNegra, color="orange", alpha=0.1)
plt.xlabel('Turnos')
plt.ylabel('Fichas')
plt.title('Partida de Ajedrez')
plt.legend()
imprimir_tablero(tablero)
plt.show()
input("Presiona Enter para salir...")

