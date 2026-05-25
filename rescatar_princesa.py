import random

####################################

def mostrar_mapa():
    print('####################################')
    for fila in mapa:
        print('   '.join(fila))  # Dos espacios en lugar de uno

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

    while pociones_en_mapa < municion_inicial :
        fila = random.randint(0, tamano_mapa - 1)
        columna = random.randint(0, tamano_mapa  -1)

        if mapa[fila][columna] == '🌲':
        
            mapa[fila][columna] = mi_municion
            pociones_en_mapa += 1

def buscar_caballero():
    for fila in range(tamano_mapa):
        for columna in range(tamano_mapa):
            if mapa[fila][columna] in (mi_personaje,'🛡️ '):
                return fila, columna

def comprobar_movimiento(fila, columna):

    global heroe

    if mi_personaje == '⚔️ ':
        if mapa[fila][columna] == mi_municion:
            heroe['ataques'] += 1
            mapa[fila][columna] = '⚔️ '
            return mapa[fila][columna]
        elif mapa[fila][columna] in ('🐉', '🐲'):
            if heroe['ataques'] > 0: # Me quedan ataques por realizar:
                es_movil = mapa[fila][columna] == '🐲'
                drop_municion(es_movil)
                mapa[fila][columna] = '⚔️ '
                heroe['ataques'] -= 1
            else:
                mapa[fila][columna] = '☠️'
            return mapa[fila][columna]
        elif mapa[fila][columna] == '👸':
            return '👸'
        else:
            return '⚔️ '
        
    elif mi_personaje == '🏹':
        if mapa[fila][columna] == mi_municion:
            heroe['ataques'] += 1
            mapa[fila][columna] = '🏹'
            return mapa[fila][columna]
        elif mapa[fila][columna] in ('🐉', '🐲'):
            mapa[fila][columna] = '☠️'
            return mapa[fila][columna]
        elif mapa[fila][columna] == '👸':
            return '👸'
        else:
            return '🏹'

def movimiento_caballero(movimiento):

    fila, columna = buscar_caballero()
    nueva_fila, nueva_columna = fila, columna

    if movimiento.lower() not in ('w', 's', 'a', 'd'):
        return 'invalido'
    
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

    global heroe, princesa_muerta

    try:
        fila, columna = buscar_caballero()
        if ultimo_movimiento.lower() == 'a' and columna - 2 < 0:
            raise IndexError
        elif ultimo_movimiento.lower() == 'w' and fila - 2 < 0:
            raise IndexError
        
        if ultimo_movimiento.lower() == 'a':
            # ataca dos casillas a la izquierda
            
            if mapa[fila][columna - 2] == '👸':
                mapa[fila][columna - 2] = '🪦'
                princesa_muerta = True
            else:

                if mapa[fila][columna - 2] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila and datos['columna'] == columna - 2:
                            es_movil = mapa[fila][columna - 2] == '🐲'
                            drop_municion(es_movil)
                            datos['vivo'] = False
                            break
                mapa[fila][columna -2] = '🌲'

        elif ultimo_movimiento.lower() == 'd':
            # ataca dos casillas a la derecha
            if mapa[fila][columna + 2] == '👸':
                mapa[fila][columna + 2] = '🪦'
                princesa_muerta = True
            else:
                if mapa[fila][columna + 2] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila and datos['columna'] == columna + 2:
                            es_movil = mapa[fila][columna + 2] == '🐲'
                            drop_municion(es_movil)
                            datos['vivo'] = False
                            break
                mapa[fila][columna + 2] = '🌲'

        elif ultimo_movimiento.lower() == 'w':
            # ataca dos casillas arriba
            if mapa[fila - 2][columna] == '👸':
                mapa[fila - 2][columna] = '🪦'
                princesa_muerta = True
            else:
                if mapa[fila - 2][columna] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila - 2 and datos['columna'] == columna:
                            es_movil = mapa[fila - 2][columna] == '🐲'
                            drop_municion(es_movil)
                            datos['vivo'] = False
                            break
                mapa[fila - 2][columna] = '🌲'

        elif ultimo_movimiento.lower() == 's':
            # ataca dos casillas hacia abajo
            if mapa[fila + 2][columna] == '👸':
                mapa[fila + 2][columna] = '🪦'
                princesa_muerta = True
            else:
                if mapa[fila + 2][columna] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila + 2 and datos['columna'] == columna:
                            es_movil = mapa[fila + 2][columna] == '🐲'
                            drop_municion(es_movil)
                            datos['vivo'] = False
                            break
                mapa[fila + 2][columna] = '🌲'

        heroe['ataques'] -= 1

    except IndexError:
        print ('Has fallado el ataque.')
        heroe['ataques'] -= 1

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

    if mi_personaje == '⚔️ ':
        movimiento = input('W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA), H (Habilidad Especial): ')
    elif mi_personaje == '🏹':
        movimiento = input('W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA), E (ATAQUE), H (Habilidad Especial): ')
    
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
    if mi_personaje == '⚔️ ':
        return '🗡️ '
    elif mi_personaje == '🏹':
        return '➶ '    
    else:
        return '❤️'

def selector_dragon_movil():
    dragones = {}
    num_dragones = 0
    
    while num_dragones < max_dragones_moviles:
        for i in range(tamano_mapa):
            for j in range(tamano_mapa):
                if mapa[i][j] == '🐉':
                    if random.randint(0, 10) == 10:
                        mapa[i][j] = '🐲'
                        num_dragones += 1
                        dragones[f'dragon{num_dragones}'] = {
                        'fila': i,
                        'columna': j,
                        'vivo': True
                        }  
                        if num_dragones == max_dragones_moviles:
                            break
            if num_dragones == max_dragones_moviles:
                break
    return dragones

def comprobar_movimiento_dragon(fila_dragon, columna_dragon):

    global heroe

    if mapa[fila_dragon][columna_dragon] == '🌲':
        return None
    if mapa[fila_dragon][columna_dragon] == '👸':
        mapa[fila_dragon][columna_dragon] = '🪦'
        return '🪦'
    elif mapa[fila_dragon][columna_dragon] == '🏹':
        mapa[fila_dragon][columna_dragon] = '☠️'
        return '☠️'
    elif mapa[fila_dragon][columna_dragon]  in (mi_personaje, '🛡️ '):
        if heroe['escudo_activo']:  # Escudo activo: el dragón muere siempre
            mapa[fila_dragon][columna_dragon] = mi_personaje
            heroe['escudo_activo'] = False
            return 'dragon_muerto'
        elif heroe['ataques'] > 0:
            mapa[fila_dragon][columna_dragon] = mi_personaje
            heroe['ataques'] -= 1
            return 'dragon_muerto'
        else:
            mapa[fila_dragon][columna_dragon] = '☠️'
            return '☠️'
    
def movimiento_dragon():
    ### Movimiento dragon 1
    ## El dragón se mueve aleatoriamente una casilla, pudiendo ser arriba, abajo, izquierda o derecha.Solo
    ## se puede mover a una zona de árbol. En caso de no haber casillas que cumplan esa condición, no se moverá.
    ## Lanzamos un aleatorio de 0,3 -> 0 (izquierda), 1 (derecha), 2 (arriba), 3 (abajo).


    for nombre_dragon, datos in dragones_moviles.items():
        filaDragon = datos['fila']
        columnaDragon = datos['columna']

        if not datos['vivo']:
            continue

        check_movimiento = None

        if mapa[filaDragon][columnaDragon] != '🐲':  # El dragón ya no existe
            datos['vivo'] = False
            continue

        movimiento_dragon = False
        contador_movimientos = 0
        try:

            filaHeroe, columnaHeroe = buscar_caballero()
            distancia = abs(filaDragon - filaHeroe) + abs(columnaDragon - columnaHeroe)

            if heroe['escudo_activo'] and distancia <= heroe['radio_taunt']:
                direcciones = [direccion_hacia_heroe(filaDragon, columnaDragon, filaHeroe, columnaHeroe)]
            else:
                direcciones = [0, 1, 2, 3]
                random.shuffle(direcciones)

            for mueve_dragon in direcciones:
                if mueve_dragon == 0 and columnaDragon - 1 >= 0 and mapa[filaDragon][columnaDragon - 1] in ('🌲', '🛡️ ',mi_personaje, '👸'): ### izquierda
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon,columnaDragon - 1)
                    if check_movimiento is None:
                        mapa[filaDragon][columnaDragon -1] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon - 1
                    movimiento_dragon = True
                    break
                elif mueve_dragon == 1 and mapa[filaDragon][columnaDragon + 1]  in ('🌲', '🛡️ ', mi_personaje, '👸'): ## derecha
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon,columnaDragon + 1)
                    if check_movimiento is None:
                        mapa[filaDragon][columnaDragon +1] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon + 1
                    movimiento_dragon = True
                    break
                elif mueve_dragon == 2 and filaDragon - 1 >= 0 and mapa[filaDragon - 1][columnaDragon] in ('🌲', '🛡️ ', mi_personaje, '👸'): ## arriba
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon - 1,columnaDragon)
                    if check_movimiento is None:
                        mapa[filaDragon - 1][columnaDragon] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon - 1
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon
                    movimiento_dragon = True
                    break
                elif mueve_dragon == 3 and mapa[filaDragon + 1][columnaDragon]  in ('🌲','🛡️ ',  mi_personaje, '👸'):
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon + 1,columnaDragon)
                    if check_movimiento is None:
                        mapa[filaDragon + 1][columnaDragon] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon + 1
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon
                    movimiento_dragon = True    
                    break

        except IndexError:
            pass

        if check_movimiento in ('☠️', '🪦'):
            return check_movimiento
        elif check_movimiento == 'dragon_muerto':
            dragones_moviles[nombre_dragon]['vivo'] = False
        
    for nombre_dragon, datos in dragones_moviles.items():
        if not datos['vivo']:
            reasignar_dragon_movil(nombre_dragon)


def reasignar_dragon_movil(nombre_dragon):
    # Comprobar si quedan dragones estáticos
    hay_dragones = any(mapa[i][j] == '🐉' for i in range(tamano_mapa) for j in range(tamano_mapa))
    
    if not hay_dragones:
        return  # No hay dragones para reasignar
    
    encontrado = False
    while not encontrado:
        for i in range(tamano_mapa):
            for j in range(tamano_mapa):
                if mapa[i][j] == '🐉':
                    if random.randint(0, 10) == 10:
                        mapa[i][j] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = i
                        dragones_moviles[nombre_dragon]['columna'] = j
                        dragones_moviles[nombre_dragon]['vivo'] = True
                        encontrado = True
                        break
            if encontrado:
                break

def drop_municion(es_movil):

    # Calcular max_municion dinámicamente según dragones vivos
    dragones_vivos = sum(1 for datos in dragones_moviles.values() if datos['vivo'])

    max_municion_actual = dragones_vivos // 2

    # Contar municiones actuales en el mapa
    municion_en_mapa = sum(1 for i in range(tamano_mapa) for j in range(tamano_mapa) if mapa[i][j] == mi_municion)
    
    if municion_en_mapa >= max_municion_actual:
        return  # Ya hay suficiente munición
    
    # Probabilidad según tipo de dragón
    probabilidad = 4 if es_movil else 6
    
    if random.randint(1, probabilidad) == 1:
        # Buscar casilla vacía aleatoria
        encontrado = False
        while not encontrado:
            fila = random.randint(0, tamano_mapa - 1)
            columna = random.randint(0, tamano_mapa - 1)
            if mapa[fila][columna] == '🌲':
                mapa[fila][columna] = mi_municion
                encontrado = True

def habilidad_especial():

    print(f'Habilidades disponibles: {heroe["habilidades_especiales"]}')
    if mi_personaje == '⚔️ ':
        if heroe['habilidades_especiales'] > 0:
            heroe['escudo_activo'] = True
            filaHeroe, ColumnaHeroe = buscar_caballero()
            mapa[filaHeroe][ColumnaHeroe] = '🛡️ '
            heroe['habilidades_especiales'] -= 1

def direccion_hacia_heroe(filaDragon, columnaDragon, filaHeroe, columnaHeroe):
    diff_fila = filaHeroe - filaDragon
    diff_columna = columnaHeroe - columnaDragon
    
    if abs(diff_fila) >= abs(diff_columna):
        return 2 if diff_fila < 0 else 3  # arriba o abajo
    else:
        return 0 if diff_columna < 0 else 1  # izquierda o derecha
################################

lista_personajes = ('⚔️ ','🏹','🧙')

print('¡Bienvenido héroe! Debes rescatar a la princesa pasando a través de feroces dragones.')
print(lista_personajes[0],' : El caballero es un luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gastas un ataque por cada dragón derrotado.')
print(lista_personajes[1],' : El arquero es un luchador a distancia. Para atacar selecciona el botón de ataque (E).',end= ' ')
print('Solo puede atacar en la dirección del último movimiento realizado y únicamente a dos posiciones respecto a la actual.', end= ' ')
print('Si el primer movimiento es un ataque se hará hacia la derecha. El ataque se reduce aunque falles el golpe.')
print(lista_personajes[2],' : Contenido bloqueado. Compra el DLC para desbloquearlo.')
print('❤️: Si pasas sobre un corazón recuperas 1 punto de ataque')
#######################

print('🌲', '🐉', '🐲', '⚔️ ', '🏹', '🧙', '👸', '🏰', '☠️', '🪦', '🗡️ ', '➶ ', '❤️')
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
        municion_inicial  = 1
        max_dragones_moviles = 1
        max_habilidades = 0
    elif dificultad == 1:
        tamano_mapa = 10
        num_dragones = 10
        municion_inicial  = 3
        max_dragones_moviles  = 2
        max_habilidades = 1
        
    max_municion = max_dragones_moviles // 2

    if mi_personaje == '⚔️ ':
        heroe = {
            'ataques': 3,
            'habilidades_especiales': max_habilidades,
            'nivel': 1,
            'experiencia': 0,
            'escudo_activo': False,
            'radio_taunt': 4,
            'distancia_disparo': None
        }
    elif mi_personaje == '🏹':
            heroe = {
                'ataques': 3,
                'habilidades_especiales': max_habilidades,
                'nivel': 1,
                'experiencia': 0,
                'escudo_activo': None,
                'radio_taunt': None,
                'distancia_disparo': 2
    }
            
    mapa = [['🌲'] * tamano_mapa for _ in range(tamano_mapa)]

    print('Personaje elegido: ', mi_personaje)


    print(f'Vamos a rescatar a la princesa. Dispone de {heroe["ataques"]} ataques')

    cargar_mapa()
    dragones_moviles = selector_dragon_movil()
    print('Mapa cargado')
    mostrar_mapa()


    ultimo_movimiento = 'd' # Como dijimos que el primer ataque, si no se ha movido antes es hacia la derecha lo inicializamos
    movimiento = seleccionar_movimiento()  # Primera jugada antes del bucle
    if heroe['ataques'] < 0:
        heroe['ataques'] = 0

    while True:
        print(f'Inicio bucle, movimiento: {movimiento}')  # Debug
        if movimiento.lower() == 'e':
            print(f'Dispone de {heroe["ataques"]} ataques')
            if princesa_muerta:
                print('¡Has matado a la princesa!')
                mostrar_mapa()
                break
            resultado_dragon = movimiento_dragon()
            if resultado_dragon == '☠️':
                print('El héroe ha sido atrapado por el dragón')
                mostrar_mapa()
                break
            elif resultado_dragon == '🪦':
                print('El dragón ha llegado antes a la princesa')
                mostrar_mapa()
                break
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        elif movimiento.lower() == 'h':
            if heroe['habilidades_especiales'] == 0:
                print('No tienes habilidades especiales disponibles')
                mostrar_mapa()
                movimiento = seleccionar_movimiento()
                continue
            habilidad_especial()
            resultado_dragon = movimiento_dragon()
            if resultado_dragon == '☠️':
                print('El héroe ha sido atrapado por el dragón')
                mostrar_mapa()
                break
            elif resultado_dragon == '🪦':
                print('El dragón ha llegado antes a la princesa')
                mostrar_mapa()
                break
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue



        if heroe['escudo_activo']:
            resultado_dragon = movimiento_dragon()
            if resultado_dragon == '🪦':
                print('El dragón ha llegado antes a la princesa')
                mostrar_mapa()
                break
            print(f'Dispone de {heroe["ataques"]} ataques')
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue

        resultado_heroe = movimiento_caballero(movimiento)
            
        
        if resultado_heroe == 'invalido':
            print('Movimiento no válido')
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue

        if resultado_heroe == '☠️':
            print('El héroe ha perdido')
            mostrar_mapa()
            break
        elif resultado_heroe == '👸':
            mapa[tamano_mapa - 1][tamano_mapa - 1] = '🏰'
            print('¡Princesa rescatada!')
            mostrar_mapa()
            break
        elif resultado_heroe == '🪦':
            print('¡Has matado a la princesa!')
            mostrar_mapa()
            break      


        resultado_dragon = movimiento_dragon()
        

        if resultado_dragon == '☠️':
            print('El héroe ha sido atrapado por el dragón')
            mostrar_mapa()
            break
        elif resultado_dragon == '🪦':
            print('El dragón ha llegado antes a la princesa')
            mostrar_mapa()
            break 

        print(f'Dispone de {heroe["ataques"]} ataques')
        mostrar_mapa()
        
        movimiento = seleccionar_movimiento()