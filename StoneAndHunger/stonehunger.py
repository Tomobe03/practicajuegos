# TOP DOWN:
import random
from datetime import datetime

def iniciarJuego():
    print("Piedra, Papel o Tijera: Terror and Starvation!\n", end="")
    print("    By Tomobe03 y Rata de Sanja.\n\n", end="")
    random.seed(datetime.now().timestamp())
    
"""
def mostrarMapa(map):
    print("    ", end="")
    for caracter in map:
        print(f"{caracter}  ", end="")
    print("\n\n", end="")
"""
def hacerPPT():
    piedra = 1
    papel = 2
    tijera = 3
    ganador = -1
    while ganador == -1:
        usuario = int(input(f"Elegir piedra ({piedra}), papel ({papel}) o tijera ({tijera}): "))
        ia = random.choice([piedra,papel,tijera])
        mostrarEleccion(usuario, ia)
        if usuario == ia:
            ganador = -1 # empate
            print("Empate!\n", end="")
        elif (usuario == piedra and ia == tijera) or (usuario == tijera and ia == papel) or (usuario == papel and ia == piedra):
            ganador = 0 # victoria
        else:
            ganador = 1 # derrota
    return ganador

def mostrarEleccion(u, i):
    lista = ["Piedra", "Papel", "Tijera"]
    print(f"{lista[u-1]} - {lista[i-1]}\n", end="")

def mostrarGanadorPPT(ganador):
    if ganador == 0:
        print("Victoria! :)\n")
    else:
        print("Derrota! :(\n")
        
def moverJugadores(map, contador): # Si el ganador es 0, mover hacia la derecha. Si el ganador es 1, mover hacia la izquierda
    estadosPosiblesDelMapa = [
        "#xB              #",
        "#A  B            #",
        "#   A  B         #",
        "#      A  B      #",
        "#         A  B   #",
        "#            A  B#",
        "#              Ax#"]

    return estadosPosiblesDelMapa[contador + 3]

def actualizarContador(ganador, contador):
    if ganador == 0:
        return contador + 1
    else:
        return contador - 1
        
if __name__ == "__main__":
    iniciarJuego()
    mapa = "#      A  B      #"
    print(f"{mapa}\n")
    contador = 0
    while contador > -3 and contador < 3: # Loop en el que se hacen las rondas
        ganadorDeRonda = hacerPPT()
        mostrarGanadorPPT(ganadorDeRonda)
        contador = actualizarContador(ganadorDeRonda, contador)
        mapa = moverJugadores(mapa, contador)
        print(f"{mapa}\n")
    print(" FIN DE JUEGO")