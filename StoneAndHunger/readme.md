# Piedra, Papel o Tijera EPICO


### Analisis
Jugas contra una IA
Cada jugador tiene su base en los extremos del mapa.
El mapa es una linea de 6 espacios, se comienza en el medio, cada uno de los jugadores ocupando un espacio.
Cada ronda el ganador del Piedra Papel o Tijera avanza un espacio en la linea y el perdedor retrocede.
El jugador que llegue primero a la base enemiga ganará la partida.

Logica del piedra papel o tijera:
    Piedra gana a Tijera
    Tijera gana a Papel
    Papel gana a Piedra
    
### Diseño
El juego corre en la terminal de windows
El mapa es una array de caracteres
El usuario esta definido como jugador A y la IA esta definida como jugador B

Hay un contador de rondas que comienza en 0
Se suma 1 cuando el usuario gana una ronda y se resta 1 cuando el usuario pierde
Si el contador llega a 3, el usuario gana la partida
Si el contador llega a -3 el usuario pierde la partida

Cada ronda se lee input del usuario:
    1. Piedra
    2. Papel
    3. Tijera

Luego se genera aleatoriamente una elección para la IA

Se evalua quien ganó, se muestra en pantalla y se avanza a la siguiente ronda
