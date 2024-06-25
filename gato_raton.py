import random

# Crear un tablero de juego
tablero_5x4 = [['*' for _ in range(5)] for _ in range(4)]

# Definir las posiciones de los personajes
posicion_g = [3, 2]  # Fila, Columna
posicion_r = [0, 0]  # Fila, Columna

# Colocar los personajes en el tablero
tablero_5x4[posicion_g[0]][posicion_g[1]] = 'G'
tablero_5x4[posicion_r[0]][posicion_r[1]] = 'R'

# Lista para almacenar los movimientos previos
movimientos_previos = []

# Función para verificar si el juego ha terminado
def terminar_juego():
    return posicion_r == posicion_g

# Función de evaluación para Minimax
def evaluar():
    distancia = abs(posicion_g[0] - posicion_r[0]) + abs(posicion_g[1] - posicion_r[1])
    return -distancia  # El gato quiere minimizar la distancia, el ratón quiere maximizarla

# Función para obtener movimientos posibles
def movimientos_posibles(posicion):
    fila, columna = posicion
    movimientos = []
    
    if fila > 0:
        movimientos.append('arriba')
    if fila < 3:
        movimientos.append('abajo')
    if columna > 0:
        movimientos.append('izquierda')
    if columna < 4:
        movimientos.append('derecha')

    return movimientos

# Función para hacer un movimiento
def hacer_movimiento(posicion, direccion):
    fila_actual, columna_actual = posicion

    if direccion == 'arriba':
        fila_actual -= 1
    elif direccion == 'abajo':
        fila_actual += 1
    elif direccion == 'izquierda':
        columna_actual -= 1
    elif direccion == 'derecha':
        columna_actual += 1

    return [fila_actual, columna_actual]

# Algoritmo Minimax
def minimax(posicion_g, posicion_r, profundidad, max_jugador):
    if profundidad == 0 or terminar_juego():
        return evaluar()
    
    if max_jugador:  # Turno del gato
        max_eval = float('-inf')
        for movimiento in movimientos_posibles(posicion_g):
            nueva_posicion_g = hacer_movimiento(posicion_g, movimiento)
            eval = minimax(nueva_posicion_g, posicion_r, profundidad - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    
    else:  # Turno del ratón
        min_eval = float('inf')
        for movimiento in movimientos_posibles(posicion_r):
            nueva_posicion_r = hacer_movimiento(posicion_r, movimiento)
            eval = minimax(posicion_g, nueva_posicion_r, profundidad - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# Función para encontrar el mejor movimiento usando Minimax
def mejor_movimiento(posicion, profundidad, max_jugador):
    mejor_movimiento = None
    if max_jugador:  # Turno del gato
        mejor_eval = float('-inf')
        for movimiento in movimientos_posibles(posicion):
            nueva_posicion = hacer_movimiento(posicion, movimiento)
            eval = minimax(nueva_posicion, posicion_r, profundidad - 1, False)
            if eval > mejor_eval:
                mejor_eval = eval
                mejor_movimiento = movimiento
    else:  # Turno del ratón
        mejor_eval = float('inf')
        for movimiento in movimientos_posibles(posicion):
            nueva_posicion = hacer_movimiento(posicion, movimiento)
            eval = minimax(posicion_g, nueva_posicion, profundidad - 1, True)
            if eval < mejor_eval:
                mejor_eval = eval
                mejor_movimiento = movimiento
    return mejor_movimiento

# Definir la profundidad de búsqueda para Minimax
profundidad = 3

# Bucle principal del juego
for turno in range(5):
    # Movimiento del gato
    if random.random() < 0.1:  # probabilidad de atrapar al ratón
        tablero_5x4[posicion_g[0]][posicion_g[1]] = '*'
        posicion_g = posicion_r[:]
    else:
        movimiento_g = mejor_movimiento(posicion_g, profundidad, True)
        nueva_posicion_g = hacer_movimiento(posicion_g, movimiento_g)
       
        tablero_5x4[posicion_g[0]][posicion_g[1]] = '*'
        posicion_g = nueva_posicion_g

    tablero_5x4[posicion_g[0]][posicion_g[1]] = 'G'

    # Verificar si el juego ha terminado
    if terminar_juego():
        print("¡El gato atrapó al ratón!")
        break

    # Movimiento del ratón
    movimiento_r = mejor_movimiento(posicion_r, profundidad, False)
    nueva_posicion_r = hacer_movimiento(posicion_r, movimiento_r)
    tablero_5x4[posicion_r[0]][posicion_r[1]] = '*'
    posicion_r = nueva_posicion_r
    tablero_5x4[posicion_r[0]][posicion_r[1]] = 'R'

    # Verificar si el juego ha terminado
    if terminar_juego():
        print("¡El ratón escapó del gato!")
        break

    # Imprimir el tablero de juego actual y los movimientos previos
    for fila in tablero_5x4:
        print(" ".join(fila))
    for movimiento in movimientos_previos:
        print(movimiento)
    print()

# Si el bucle termina sin que el juego haya terminado
if not terminar_juego():
    print("El ratón se escapó del gato en 5 turnos.")

# Imprimir el tablero de juego final
for fila in tablero_5x4:
    print(" ".join(fila))

