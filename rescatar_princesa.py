import random

####################################

def mostrar_mapa():
    print('####################################')
    for fila in mapa:
        print(' '.join(fila))  # Dos espacios en lugar de uno

def cargar_mapa():
    
    dragones_en_mapa = 0
    pociones_en_mapa = 0

    mapa[0][0] = mi_personaje
    mapa[tamano_mapa -1 ][tamano_mapa - 1 ] = '👸'

    while dragones_en_mapa < num_dragones:
        fila = random.randint(0, tamano_mapa -1)
        columna = random.randint(0, tamano_mapa -1)

        if mapa[fila][columna] == '🌲':
        
           mapa[fila][columna] = '🐉'
           dragones_en_mapa += 1

    while pociones_en_mapa < num_pociones:
        fila = random.randint(0, tamano_mapa - 1)
        columna = random.randint(0, tamano_mapa  -1)

        if mapa[fila][columna] == '🌲':
        
           mapa[fila][columna] = mi_municion
           pociones_en_mapa += 1

def buscar_caballero():
    for fila in range(tamano_mapa):
        for columna in range(tamano_mapa):
            if mapa[fila][columna] == mi_personaje:
                return fila, columna

def comprobar_movimiento(fila, columna):

    global ataques

    if mi_personaje == '⚔️':
        if mapa[fila][columna] == mi_municion:
            ataques += 1
            mapa[fila][columna] = '⚔️'
            return mapa[fila][columna]
        elif mapa[fila][columna] == '🐉':
            if ataques > 0: # Me quedan ataques por realizar:
                mapa[fila][columna] = '⚔️'
                ataques -= 1
            else:
                mapa[fila][columna] = '☠️'

            return mapa[fila][columna]
        elif mapa[fila][columna] == '👸':
            return '👸'
        else:
            return '⚔️'
        
    elif mi_personaje == '🏹':
        if mapa[fila][columna] == mi_municion:
            ataques += 1
            mapa[fila][columna] = '🏹'
            return mapa[fila][columna]
        elif mapa[fila][columna] == '🐉':
            mapa[fila][columna] = '☠️'
            return mapa[fila][columna]
        elif mapa[fila][columna] == '👸':
            return '👸'
        else:
            return '🏹'

def movimiento_caballero(movimiento):

    fila, columna = buscar_caballero()
    nueva_fila, nueva_columna = fila, columna

    if movimiento.lower() == 'w':
        nueva_fila = fila - 1
    elif movimiento.lower() == 's':
        nueva_fila = fila + 1
    elif movimiento.lower() == 'a':
        nueva_columna = columna - 1
    elif movimiento.lower() == 'd':
        nueva_columna = columna + 1

    try:
        if nueva_fila < 0 or nueva_columna < 0:
            raise IndexError

        resultado = comprobar_movimiento(nueva_fila, nueva_columna)
        mapa[fila][columna] = '🌲'

        if resultado == '☠️':
            mapa[nueva_fila][nueva_columna] = '☠️'
            return '☠️'
        elif resultado == '👸':
            return '👸'
        else:
            mapa[nueva_fila][nueva_columna] = mi_personaje

    except IndexError:
        print("No puedes moverte fuera del mapa")
    
def ataque_arquero():

    global ataques, princesa_muerta

    try:
        fila, columna = buscar_caballero()
        if ultimo_movimiento.lower() == 'a' and columna - 2 < 0:
            raise IndexError
        elif ultimo_movimiento.lower() == 'w' and fila - 2 < 0:
            raise IndexError
        
        if ultimo_movimiento.lower() == 'a':
            # ataca dos casillas a la izquierda
            
            if mapa[fila][columna -2] == '👸':
                mapa[fila][columna -2] = '🪦'
                princesa_muerta = True
            else:
                mapa[fila][columna -2] = '🌲'

        elif ultimo_movimiento.lower() == 'd':
            # ataca dos casillas a la derecha
            if mapa[fila][columna + 2] == '👸':
                mapa[fila][columna + 2] = '🪦'
                princesa_muerta = True
            else:
                mapa[fila][columna + 2] = '🌲'

        elif ultimo_movimiento.lower() == 'w':
            # ataca dos casillas arriba
            if mapa[fila - 2][columna] == '👸':
                mapa[fila - 2][columna] = '🪦'
                princesa_muerta = True
            else:
                mapa[fila - 2][columna] = '🌲'

        elif ultimo_movimiento.lower() == 's':
            # ataca dos casillas hacia abajo
            if mapa[fila + 2][columna] == '👸':
                mapa[fila + 2][columna] = '🪦'
                princesa_muerta = True
            else:
                mapa[fila + 2][columna] = '🌲'
        ataques -= 1

    except IndexError:
        print ('Has fallado el ataque.')
        ataques -= 1

def selector_de_personaje():

    while True:
        try:
            mi_personaje = int(input(f'Selecciona un personaje (0:{lista_personajes[0]} 1:{lista_personajes[1]} 2:{lista_personajes[2]}): '))
            if mi_personaje in (0, 1, 2):
                return lista_personajes[mi_personaje]
            else:
                print('Opción no válida, elige 0, 1 o 2')
        except ValueError:
            print('Debes introducir un número')

def seleccionar_movimiento():

    global movimiento
    global ultimo_movimiento

    if mi_personaje == '⚔️':
        movimiento = input('W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA): ')
    elif mi_personaje == '🏹':
        movimiento = input('W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA), E (ATAQUE): ')
    
        if movimiento.lower() == 'e':
            ataque_arquero()
        else:
            ultimo_movimiento = movimiento
    return movimiento

def selector_dificultad():
    while True:
        try:
            dificultad = int(input('Selecciona dificultad (0: Fácil, 1: Media): '))
            if dificultad in (0, 1):
                return dificultad
            else:
                print('Opción no válida, elige 0 o 1')
        except ValueError:
            print('Debes introducir un número')

def selector_municion():
    if mi_personaje == '⚔️':
        return '🗡️'
    elif mi_personaje == '🏹':
        return '➶'    
    else:
        return '❤️'

################################

# mapa = [
#     ['🌲', '🌲', '🌲','🌲','🌲'],
#     ['🌲', '🌲', '🌲','🌲','🌲'],
#     ['🌲', '🌲', '🌲','🌲','🌲'],
#     ['🌲', '🌲', '🌲','🌲','🌲'],
#     ['🌲', '🌲', '🌲','🌲','🌲']
# ]

lista_personajes = ('⚔️','🏹','🧙')

print('¡Bienvenido héroe! Debes rescatar a la princesa pasando a través de feroces dragones.')
print(lista_personajes[0],' : El caballero es un luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gastas un ataque por cada dragón derrotado.')
print(lista_personajes[1],' : El arquero es un luchador a distancia. Para atacar selecciona el botón de ataque (E).',end= ' ')
print('Solo puede atacar en la dirección del último movimiento realizado y únicamente a dos posiciones respecto a la actual.', end= ' ')
print('Si el primer movimiento es un ataque se hará hacia la derecha. El ataque se reduce aunque falles el golpe.')
print(lista_personajes[2],' : Contenido bloqueado. Compra el DLC para desbloquearlo.')
print('❤️: Si pasas sobre un corazón recuperas 1 punto de ataque')
#######################

princesa_muerta = False

mi_personaje = selector_de_personaje()
mi_municion = selector_municion()

if mi_personaje == '🧙':
    print('Se le abrirá el navegador para que introduzca sus datos bancarios y desbloquear el DLC')
else:

    dificultad = selector_dificultad()

    if dificultad == 0:
        tamano_mapa = 5
        num_dragones = 5
        num_pociones = 1
    elif dificultad == 1:
        tamano_mapa = 10
        num_dragones = 10
        num_pociones = 3

    mapa = [['🌲'] * tamano_mapa for _ in range(tamano_mapa)]

    print('Personaje elegido: ', mi_personaje)

    ataques = 3

    print(f'Vamos a rescatar a la princesa. Dispone de {ataques} ataques')

    cargar_mapa()
    print('Mapa cargado')
    mostrar_mapa()


    ultimo_movimiento = 'd' # Como dijimos que el primer ataque, si no se ha movido antes es hacia la derecha lo inicializamos
    movimiento = seleccionar_movimiento()  # Primera jugada antes del bucle
    if ataques < 0:
        ataques = 0

    while True:
        if movimiento.lower() == 'e':
            print(f'Dispone de {ataques} ataques')
            mostrar_mapa()
            if princesa_muerta:
                print('¡Has matado a la princesa!')
                break
            movimiento = seleccionar_movimiento()
            continue

        resultado = movimiento_caballero(movimiento)
        
        if resultado == '☠️':
            print('El héroe ha perdido')
            mostrar_mapa()
            break
        elif resultado == '👸':
            mapa[tamano_mapa - 1][tamano_mapa - 1] = '🏰'
            print('¡Princesa rescatada!')
            mostrar_mapa()
            break
        elif resultado == '🪦':
            print('¡Has matado a la princesa!')
            mostrar_mapa()
            break
        else:
            print(f'Dispone de {ataques} ataques')
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
        
