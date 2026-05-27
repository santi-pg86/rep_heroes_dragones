# Rescatar a la Princesa
# Copyright (C) 2026 Santiago Pérez García

import random
import os
import subprocess

def limpiar_pantalla():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def obtener_nombre_fichero(nombre, personaje):
    tipos = {'⚔️ ': 'caballero', '🏹': 'arquero', '🧙': 'mago'}
    tipo = tipos[personaje]
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves_heroes_dragones', f'{nombre}_{tipo}.txt')

def cargar_save(nombre, personaje):
    fichero = obtener_nombre_fichero(nombre, personaje)
    if os.path.exists(fichero):
        while (opcion := input(f'Se encontró una partida guardada para {nombre}. ¿Quieres cargarla? (S/N): ').upper()) not in ('S', 'N'):
            print('Opción no válida')
        if opcion == 'S':
            with open(fichero, 'r') as f:
                datos = f.read().split('#')
                return int(datos[0]), int(datos[1]), int(datos[2])  # nivel, pantalla, xp
    return None

def guardar_save(nombre, personaje, nivel, pantalla_max, xp):
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves_heroes_dragones')
    os.makedirs(carpeta, exist_ok=True)
    fichero = obtener_nombre_fichero(nombre, personaje)
    with open(fichero, 'w') as f:
        f.write(f'{nivel}#{pantalla_max}#{xp}#')

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

    if mi_personaje in ('⚔️ ','🏹','🧙'):
        if mapa[fila][columna] == mi_municion:
            heroe['ataques'] += 1
            mapa[fila][columna] = mi_personaje
            return mapa[fila][columna]
        elif mapa[fila][columna] in ('🐉', '🐲') and mi_personaje == '⚔️ ' and  heroe['ataques'] > 0:
            es_movil = mapa[fila][columna] == '🐲'
            drop_municion(es_movil)
            ganar_xp(50 if es_movil else 10)
            mapa[fila][columna] = '⚔️ '
            heroe['ataques'] -= 1
            return mapa[fila][columna]
        elif mapa[fila][columna] in ('🐉', '🐲'):
            mapa[fila][columna] = '☠️ '
            return mapa[fila][columna]
        elif mapa[fila][columna] == '👸':
            return '👸'
        elif mapa[fila][columna] == '🐺':
            return '🐺'
        else:
            return mi_personaje

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

        if resultado == '☠️ ':
            mapa[nueva_fila][nueva_columna] = '☠️ '
            return '☠️ '
        elif resultado == '👸':
            return '👸'
        elif resultado == '🐺':
            mapa[nueva_fila][nueva_columna] = '🐺'
            mapa[fila][columna] = mi_personaje  # restaurar al héroe
            print('¡Un lobo aliado bloquea el paso!')
            return 'invalido'
        else:
            mapa[nueva_fila][nueva_columna] = mi_personaje

    except IndexError:
        print("No puedes moverte fuera del mapa")

def ataque_E():
    global heroe, princesa_muerta

    fila, columna = buscar_caballero()

    if ultimo_movimiento.lower() == 'a':
        df, dc = 0, -1
    elif ultimo_movimiento.lower() == 'd':
        df, dc = 0, 1
    elif ultimo_movimiento.lower() == 'w':
        df, dc = -1, 0
    elif ultimo_movimiento.lower() == 's':
        df, dc = 1, 0

    try:
        for i in range(2, heroe['distancia_disparo_E'] + 1):
            fila_obj = fila + df * i
            columna_obj = columna + dc * i
            if fila_obj < 0 or columna_obj < 0:
                raise IndexError
            if mapa[fila_obj][columna_obj] == '👸':
                mapa[fila_obj][columna_obj] = '🪦'
                princesa_muerta = True
                break
            elif mapa[fila_obj][columna_obj] in ('🐉', '🐲'):
                if mapa[fila_obj][columna_obj] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila_obj and datos['columna'] == columna_obj:
                            datos['vivo'] = False
                            drop_municion(True)
                            ganar_xp(50)
                            break
                else:
                    drop_municion(False)
                    ganar_xp(10)
                mapa[fila_obj][columna_obj] = '🌲'
                break
        heroe['ataques'] -= 1
    except IndexError:
        print('Has fallado el ataque.')
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
    elif mi_personaje in ('🏹','🧙'):
        direcciones_texto = {'w': 'ARRIBA', 's': 'ABAJO', 'a': 'IZQUIERDA', 'd': 'DERECHA'}
        dir_texto = direcciones_texto.get(ultimo_movimiento.lower(), 'DERECHA')
        movimiento = input(f'W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA), E (ATAQUE {dir_texto}), H (Habilidad Especial): ')
    
        if movimiento.lower() == 'e':
            if heroe['ataques'] <= 0:
                print('No tienes ataques disponibles')
                return seleccionar_movimiento()
            else:
                ataque_E()
        else:
            if movimiento.lower() not in ('e', 'h'):
                ultimo_movimiento = movimiento
    return movimiento

def selector_municion():
    municiones = {'⚔️ ': '🗡️ ', '🏹': '➶ ', '🧙': '⚡'}
    return municiones.get(mi_personaje, '❤️')

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
    elif mapa[fila_dragon][columna_dragon] in ('🏹','🧙'):
        mapa[fila_dragon][columna_dragon] = '☠️ '
        return '☠️ '
    elif mapa[fila_dragon][columna_dragon]  in (mi_personaje, '🛡️ '):
        if heroe['escudo_activo']:  # Escudo activo: el dragón muere siempre
            mapa[fila_dragon][columna_dragon] = '🛡️ '
            heroe['max_dragones_atraidos'] -= 1
            if heroe['max_dragones_atraidos'] <= 0:
                heroe['escudo_activo'] = False
                mapa[fila_dragon][columna_dragon] = mi_personaje
            return 'dragon_muerto'
        elif heroe['ataques'] > 0:
            mapa[fila_dragon][columna_dragon] = mi_personaje
            heroe['ataques'] -= 1
            return 'dragon_muerto'
        else:
            mapa[fila_dragon][columna_dragon] = '☠️ '
            return '☠️ '
    elif mapa[fila_dragon][columna_dragon] == '🐺':
        # eliminar la invocación
        for inv in invocaciones:
            if inv['fila'] == fila_dragon and inv['columna'] == columna_dragon:
                invocaciones.remove(inv)
                break
        mapa[fila_dragon][columna_dragon] = '🌲'
        return 'dragon_muerto'
    
def movimiento_dragon():
    ### Movimiento dragon 1
    ## El dragón se mueve aleatoriamente una casilla, pudiendo ser arriba, abajo, izquierda o derecha.Solo
    ## se puede mover a una zona de árbol. En caso de no haber casillas que cumplan esa condición, no se moverá.
    ## Lanzamos un aleatorio de 0,3 -> 0 (izquierda), 1 (derecha), 2 (arriba), 3 (abajo).

    global turnos_caos

    for nombre_dragon, datos in dragones_moviles.items():
        filaDragon = datos['fila']
        columnaDragon = datos['columna']

        if not datos['vivo']:
            continue

        check_movimiento = None

        if mapa[filaDragon][columnaDragon] != '🐲':  # El dragón ya no existe
            datos['vivo'] = False
            continue

        try:

            filaHeroe, columnaHeroe = buscar_caballero()    
            distancia = abs(filaDragon - filaHeroe) + abs(columnaDragon - columnaHeroe)

            if heroe['escudo_activo'] and distancia <= heroe['radio_taunt']:
                direccion_principal = direccion_hacia_heroe(filaDragon, columnaDragon, filaHeroe, columnaHeroe)
                otras = [d for d in [0, 1, 2, 3] if d != direccion_principal]
                random.shuffle(otras)
                direcciones = [direccion_principal] + otras
            elif turnos_caos > 0:
                direccion_principal = direccion_hacia_princesa(filaDragon, columnaDragon)
                otras = [d for d in [0, 1, 2, 3] if d != direccion_principal]
                random.shuffle(otras)
                direcciones = [direccion_principal] + otras
            else:
                direcciones = [0, 1, 2, 3]
                random.shuffle(direcciones)

            for mueve_dragon in direcciones:
                if mueve_dragon == 0 and columnaDragon - 1 >= 0 and mapa[filaDragon][columnaDragon - 1] in ('🌲', '🛡️ ',mi_personaje, '👸','🐺'): ### izquierda
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon,columnaDragon - 1)
                    if check_movimiento is None:
                        mapa[filaDragon][columnaDragon -1] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon - 1
                    break
                elif mueve_dragon == 1 and columnaDragon + 1 < tamano_mapa and mapa[filaDragon][columnaDragon + 1] in ('🌲', '🛡️ ', mi_personaje, '👸','🐺'): ## derecha

                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon,columnaDragon + 1)
                    if check_movimiento is None:
                        mapa[filaDragon][columnaDragon +1] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon + 1
                    break
                elif mueve_dragon == 2 and filaDragon - 1 >= 0 and mapa[filaDragon - 1][columnaDragon] in ('🌲', '🛡️ ', mi_personaje, '👸','🐺'): ## arriba
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon - 1,columnaDragon)
                    if check_movimiento is None:
                        mapa[filaDragon - 1][columnaDragon] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon - 1
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon
                    break
                elif mueve_dragon == 3 and filaDragon + 1 < tamano_mapa and mapa[filaDragon + 1][columnaDragon] in ('🌲','🛡️ ', mi_personaje, '👸','🐺'): ## abajo
                    mapa[filaDragon][columnaDragon] = '🌲'
                    check_movimiento = comprobar_movimiento_dragon(filaDragon + 1,columnaDragon)
                    if check_movimiento is None:
                        mapa[filaDragon + 1][columnaDragon] = '🐲'
                        dragones_moviles[nombre_dragon]['fila'] = filaDragon + 1
                        dragones_moviles[nombre_dragon]['columna'] = columnaDragon
                    break

        except IndexError:
            pass

        if check_movimiento in ('☠️ ', '🪦'):
            return check_movimiento
        elif check_movimiento == 'dragon_muerto':
            dragones_moviles[nombre_dragon]['vivo'] = False
        
    for nombre_dragon, datos in dragones_moviles.items():
        if not datos['vivo']:
            reasignar_dragon_movil(nombre_dragon)

    # Desactivar escudo si no quedan dragones móviles
    if heroe['escudo_activo']:
        dragones_vivos = sum(1 for datos in dragones_moviles.values() if datos['vivo'])
        if dragones_vivos == 0:
            heroe['escudo_activo'] = False
            filaHeroe, columnaHeroe = buscar_caballero()
            mapa[filaHeroe][columnaHeroe] = mi_personaje

    if turnos_caos > 0:
        turnos_caos -= 1


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
                        while input((f'🐉 Dragón estático en [{i}][{j}] se convierte en móvil 🐲')) != "":
                            pass
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

    if mi_personaje == '⚔️ ':
        if heroe['habilidades_especiales'] > 0:
            filaHeroe, ColumnaHeroe = buscar_caballero()
            if heroe['nivel'] >= 5:
                radio_bonus = min(heroe['ataques'], 10)
                for df, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    for r in range(1, radio_bonus + 1):
                        fila_obj, columna_obj = filaHeroe + df * r, ColumnaHeroe + dc * r
                        if 0 <= fila_obj < tamano_mapa and 0 <= columna_obj < tamano_mapa:
                            if mapa[fila_obj][columna_obj] == '🐉':
                                ganar_xp(10)
                                drop_municion(False)
                                mapa[fila_obj][columna_obj] = '🌲'
                                heroe['max_dragones_atraidos'] += 1
                                heroe['max_dragones_atraidos_nivel'] += 1   
            heroe['max_dragones_atraidos'] = heroe['max_dragones_atraidos_nivel']
            heroe['escudo_activo'] = True
            mapa[filaHeroe][ColumnaHeroe] = '🛡️ '
            heroe['habilidades_especiales'] -= 1
    elif mi_personaje == '🏹':
        if heroe['habilidades_especiales'] > 0:
            filaHeroe, ColumnaHeroe = buscar_caballero()
            habilidad_arquero_invocador()
            heroe['habilidades_especiales'] -= 1
    elif mi_personaje == '🧙':
        if heroe['habilidades_especiales'] > 0:
            filaHeroe, ColumnaHeroe = buscar_caballero()
            ataque_area_mago(filaHeroe,ColumnaHeroe)
            heroe['habilidades_especiales'] -= 1

def ataque_area_mago(fila, columna):
    global turnos_caos
    
    # Bonus nivel 5+: cada dragón móvil elimina estáticos en radio
    dragones_eliminados_bonus = 0
    if heroe['nivel'] >= 5:
        radio_bonus = min(2 * heroe['ataques'], 10)
        for datos in dragones_moviles.values():
            if datos['vivo']:
                fila_d, col_d = datos['fila'], datos['columna']
                for df, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    for r in range(1, radio_bonus + 1):
                        fila_obj = fila_d + df * r
                        col_obj = col_d + dc * r
                        if 0 <= fila_obj < tamano_mapa and 0 <= col_obj < tamano_mapa:
                            if mapa[fila_obj][col_obj] == '🐉':
                                ganar_xp(10)
                                drop_municion(False)
                                mapa[fila_obj][col_obj] = '🌲'
                                dragones_eliminados_bonus += 1

    turnos_caos = heroe['turnos_caos_nivel']
    turnos_caos = max(0, turnos_caos - (dragones_eliminados_bonus // 4))
    heroe['ataques'] = 0

    # Explosión en cruz normal
    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    try:
        for df, dc in offsets:
            for i in range(heroe['distancia_disparo'] + 1):
                fila_obj = fila + df * i
                columna_obj = columna + dc * i
                if fila_obj < 0 or columna_obj < 0:  # añadir esta línea
                    break 
                if mapa[fila_obj][columna_obj] in ('🐉', '🐲'):
                    if mapa[fila_obj][columna_obj] == '🐲':
                         for nombre_dragon, datos in dragones_moviles.items():
                            if datos['fila'] == fila_obj and datos['columna'] == columna_obj:
                                datos['vivo'] = False
                                ganar_xp(50)
                                drop_municion(False)
                    else:
                        drop_municion(False)
                        ganar_xp(10)
                    mapa[fila_obj][columna_obj] = '🌲'
    except IndexError:
        pass

def direccion_hacia_princesa(filaDragon, columnaDragon):
    filaPrincesa = tamano_mapa - 1
    columnaPrincesa = tamano_mapa - 1
    diff_fila = filaPrincesa - filaDragon
    diff_columna = columnaPrincesa - columnaDragon
    
    if abs(diff_fila) >= abs(diff_columna):
        return 2 if diff_fila < 0 else 3
    else:
        return 0 if diff_columna < 0 else 1
                        
def disparo_dirigido(fila, columna):

    while (direccion_disparo := input('Introduce la dirección del disparo W (ARRIBA), S (ABAJO), A (IZQUIERDA), D (DERECHA): ').lower()) not in ('a', 'w', 's', 'd'):
        print('Dirección no válida')

    # Calcular offset según dirección
    if direccion_disparo == 'a':
        df, dc = 0, -1
    elif direccion_disparo == 'd':
        df, dc = 0, 1
    elif direccion_disparo == 'w':
        df, dc = -1, 0
    elif direccion_disparo == 's':
        df, dc = 1, 0



    try:
        if heroe['nivel'] >= 5:
            # Primera pasada: matar todos los estáticos en el rango
            for i in range(2, heroe['distancia_disparo'] + 1):
                fila_obj = fila + df * i
                columna_obj = columna + dc * i
                if fila_obj < 0 or columna_obj < 0:
                    break
                if mapa[fila_obj][columna_obj] == '🐉':
                    drop_municion(False)
                    ganar_xp(10)
                    mapa[fila_obj][columna_obj] = '🌲'
            # Segunda pasada: parar en el primer móvil
            for i in range(2, heroe['distancia_disparo'] + 1):
                fila_obj = fila + df * i
                columna_obj = columna + dc * i
                if fila_obj < 0 or columna_obj < 0:
                    break
                if mapa[fila_obj][columna_obj] == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == fila_obj and datos['columna'] == columna_obj:
                            datos['vivo'] = False
                            drop_municion(True)
                            ganar_xp(50)
                            break
                    mapa[fila_obj][columna_obj] = '🌲'
                    break
        else:
            # nivel < 5: comportamiento original
            for i in range(2, heroe['distancia_disparo'] + 1):
            
                fila_obj = fila + df * i
                columna_obj = columna + dc * i
                if fila_obj < 0 or columna_obj < 0:
                    raise IndexError
                if mapa[fila_obj][columna_obj] in ('🐉', '🐲'):
                    if mapa[fila_obj][columna_obj] == '🐲':
                        for nombre_dragon, datos in dragones_moviles.items():
                            if datos['fila'] == fila_obj and datos['columna'] == columna_obj:
                                datos['vivo'] = False
                                drop_municion(True)
                                ganar_xp(50)
                                break
                        mapa[fila_obj][columna_obj] = '🌲'
                        break
                    else:
                        drop_municion(False)
                        ganar_xp(10)
                        mapa[fila_obj][columna_obj] = '🌲'
                        break
    except IndexError:
        pass

def direccion_hacia_heroe(filaDragon, columnaDragon, filaHeroe, columnaHeroe):
    diff_fila = filaHeroe - filaDragon
    diff_columna = columnaHeroe - columnaDragon
    
    if abs(diff_fila) >= abs(diff_columna):
        return 2 if diff_fila < 0 else 3  # arriba o abajo
    else:
        return 0 if diff_columna < 0 else 1  # izquierda o derecha
    

def mostrar_estado(mensaje_final=None, fin_partida=False):
    print(f'#################################################')
    if not fin_partida:
        dragones_estaticos = sum(1 for i in range(tamano_mapa) for j in range(tamano_mapa) if mapa[i][j] == '🐉')
        dragones_moviles_vivos = sum(1 for datos in dragones_moviles.values() if datos['vivo'])
        print(f'📍 Pantalla: {pantalla_actual}  🐉 Dragones: {dragones_estaticos}  🐲 Móviles: {dragones_moviles_vivos}')
        print(f'{mi_personaje} Ataques disponibles: {max(0, heroe["ataques"])}')
        xp_siguiente_nivel = 300 * (2 ** (heroe['nivel'] - 1))
        print(f'⭐ Nivel: {heroe["nivel"]}  XP: {heroe["experiencia"]}/{xp_siguiente_nivel}')
        if mi_personaje == '🏹':
            print(f'🏹 Ataque E: distancia {heroe["distancia_disparo_E"]}')
        if mi_personaje == '🧙':
            print(f'🧙 Ataque E: distancia {heroe["distancia_disparo_E"]}')
        if heroe['habilidades_especiales'] > 0:
            if mi_personaje == '⚔️ ':
                print(f'✨ Habilidad especial disponible: {ataque_especial} x{heroe["habilidades_especiales"]} (Radio: {heroe["radio_taunt"]}, Dragones: {heroe["max_dragones_atraidos_nivel"]})')
                if heroe['nivel'] >= 5:
                    radio_bonus = min(heroe['ataques'], 10)
                    print(f'💥 Bonus: Elimina dragones estáticos en radio {radio_bonus} antes de activar el escudo (+1 dragón absorbible por estático eliminado)')
            elif mi_personaje == '🏹':
                print(f'✨ Habilidad: {ataque_especial} x{heroe["habilidades_especiales"]} (radio: {heroe["distancia_disparo"]})')
                if heroe['nivel'] >= 5:
                    print(f'💥 Bonus: Invoca 🐺 lobos también en radio de la princesa')
            elif mi_personaje == '🧙':
                print(f'✨ Habilidad: {ataque_especial} x{heroe["habilidades_especiales"]} (radio: {heroe["distancia_disparo"]})')
                if heroe['nivel'] >= 5:
                    radio_bonus = min(2 * heroe['ataques'], 10)
                    print(f'💥 Bonus: Elimina estáticos en radio {radio_bonus} alrededor de cada dragón móvil (-1 turno caos por cada 4 eliminados)')
        if mi_personaje == '⚔️ ' and heroe['escudo_activo']:
            print(f'🛡️  Escudo activo - Inmóvil, esperando dragones ({heroe["max_dragones_atraidos"]} restantes)')
        if mi_personaje == '🧙' and turnos_caos > 0:
            print(f'⚡ PACTO DEL CAOS activo. Turnos restantes: {turnos_caos}')
    if mensaje_final:
        print(mensaje_final)
    print(f'#################################################')

def obtener_parametros_pantalla(pantalla):
    parametros_fijos = {
        1: (5, 5, 2, 2),
        2: (10, 20, 10, 5),
        3: (15, 45, 22, 12),
        4: (20, 80, 40, 20),
        5: (25, 125, 62, 32),
        6: (30, 180, 90, 45),
    }
    
    if pantalla <= 6:
        tamano, dragones, moviles, municion = parametros_fijos[pantalla]
    else:
        tamano = 30
        municion = 45
        dragones_base = 180
        for _ in range(pantalla - 6):
            dragones_base = int(dragones_base * 1.05)
        dragones = dragones_base
        moviles = -(-dragones // 2)  # redondeo hacia arriba
    
    return tamano, dragones, moviles, municion

def cargar_pantalla(pantalla_actual):
    global princesa_muerta, turnos_caos, tamano_mapa, num_dragones, max_dragones_moviles, municion_inicial, mapa,ultimo_movimiento, invocaciones

    invocaciones = []

    while (opcion := input('¿Quieres avanzar a la siguiente pantalla (A), repetir esta (R) o salir (S)? ').lower()) not in ('a', 'r', 's'):
        print('Opción no válida')

    if opcion == 's':
        guardar_save(nombre_personaje, mi_personaje, heroe['nivel'], pantalla_actual,heroe['experiencia'])  # guarda pantalla actual
        print(f'¡Hasta pronto {nombre_personaje}!')
        exit()
    if opcion == 'a':
        pantalla_actual += 1
        guardar_save(nombre_personaje, mi_personaje, heroe['nivel'], pantalla_actual,heroe['experiencia'])  # guarda pantalla_actual+1

    if opcion == 'r':
        guardar_save(nombre_personaje, mi_personaje, heroe['nivel'], pantalla_actual,heroe['experiencia'])

    tamano_mapa, num_dragones, max_dragones_moviles, municion_inicial = obtener_parametros_pantalla(pantalla_actual)
    princesa_muerta = False
    turnos_caos = 0
    ultimo_movimiento = 'd'
    heroe['ataques'] = 3
    heroe['habilidades_especiales'] = max_habilidades
    if mi_personaje == '⚔️ ':
        heroe['escudo_activo'] = False
    mapa = [['🌲'] * tamano_mapa for _ in range(tamano_mapa)]
    
    return pantalla_actual

def cargar_pantalla_derrota():
    global princesa_muerta, turnos_caos, mapa, ultimo_movimiento, invocaciones
    invocaciones = []
    while (opcion := input('¿Quieres intentarlo de nuevo (R) o salir (S)? ').lower()) not in ('r', 's'):
        print('Opción no válida')

    if opcion == 's':
        guardar_save(nombre_personaje, mi_personaje, heroe['nivel'], pantalla_actual, heroe['experiencia'])
        print(f'¡Hasta pronto {nombre_personaje}!')
        exit()
    guardar_save(nombre_personaje, mi_personaje, heroe['nivel'], pantalla_actual, heroe['experiencia'])

    princesa_muerta = False
    turnos_caos = 0
    ultimo_movimiento = 'd'
    heroe['ataques'] = 3
    heroe['habilidades_especiales'] = max_habilidades
    if mi_personaje == '⚔️ ':
        heroe['escudo_activo'] = False
    mapa = [['🌲'] * tamano_mapa for _ in range(tamano_mapa)]

def ganar_xp(cantidad):
    heroe['experiencia'] += cantidad
    xp_siguiente_nivel = 300 * (2 ** (heroe['nivel'] - 1))
    if heroe['experiencia'] >= xp_siguiente_nivel:
        heroe['nivel'] += 1
        print(f'🎉 ¡Subiste al nivel {heroe["nivel"]}!')
        if mi_personaje == '⚔️ ':
            aplicar_nivel_caballero()
        if mi_personaje == '🏹':
            aplicar_nivel_arquero()
        if mi_personaje == '🧙':
            aplicar_nivel_mago()

def aplicar_nivel_caballero():
    nivel = heroe['nivel']
    niveles = {
        1:  (3, 4, 1, 1),
        2:  (3, 4, 3, 1),
        3:  (3, 5, 5, 1),
        4:  (3, 5, 7, 1),
        5:  (3, 5, 9, 1),
        6:  (4, 5, 9, 2),
        7:  (5, 5, 9, 2),
        8:  (6, 5, 9, 3),
        9:  (7, 5, 9, 3),
        10: (8, 5, 9, 3),
    }
    ataques, radio, max_atraidos, habilidades = niveles[min(nivel, 10)]
    heroe['ataques'] = ataques
    heroe['radio_taunt'] = radio
    heroe['max_dragones_atraidos'] = max_atraidos
    heroe['max_dragones_atraidos_nivel'] = max_atraidos  # valor máximo del nivel
    heroe['habilidades_especiales'] = habilidades

def aplicar_nivel_arquero():
    nivel = heroe['nivel']
    niveles = {
        1:  (3, 3, 3, 1),
        2:  (3, 3, 3, 1),
        3:  (3, 4, 4, 1),
        4:  (3, 4, 4, 1),
        5:  (3, 5, 5, 1),
        6:  (4, 6, 6, 2),
        7:  (5, 7, 7, 2),
        8:  (6, 8, 8, 3),
        9:  (7, 9, 9, 3),
        10: (8, 10, 10, 3),
    }
    ataques, dist_e, dist_h, habilidades = niveles[min(nivel, 10)]
    heroe['ataques'] = ataques
    heroe['distancia_disparo_E'] = dist_e
    heroe['distancia_disparo'] = dist_h
    heroe['habilidades_especiales'] = habilidades

def aplicar_nivel_mago():
    nivel = heroe['nivel']
    niveles = {
        1:  (3, 2, 2, 1, 3),
        2:  (3, 3, 3, 1, 3),
        3:  (3, 3, 4, 1, 3),
        4:  (3, 3, 4, 1, 3),
        5:  (3, 4, 5, 1, 3),
        6:  (4, 4, 5, 2, 4),
        7:  (5, 4, 5, 2, 5),
        8:  (6, 4, 5, 3, 6),
        9:  (7, 4, 5, 3, 7),
        10: (8, 4, 5, 3, 8),
    }
    ataques, dist_e, radio_h, habilidades, turnos = niveles[min(nivel, 10)]
    heroe['ataques'] = ataques
    heroe['distancia_disparo_E'] = dist_e
    heroe['distancia_disparo'] = radio_h
    heroe['habilidades_especiales'] = habilidades
    heroe['turnos_caos_nivel'] = turnos

def habilidad_arquero_invocador():
    global invocaciones

    filaHeroe, columnaHeroe = buscar_caballero()
    filaPrincesa = tamano_mapa - 1
    columnaPrincesa = tamano_mapa - 1
    radio = heroe['distancia_disparo']

    # Eliminar móviles en radio del héroe
    # Eliminar móviles en radio del héroe (solo horizontal y vertical)
    for nombre_dragon, datos in dragones_moviles.items():
        if datos['vivo']:
            misma_fila = datos['fila'] == filaHeroe and abs(datos['columna'] - columnaHeroe) <= radio
            misma_columna = datos['columna'] == columnaHeroe and abs(datos['fila'] - filaHeroe) <= radio
            if misma_fila or misma_columna:
                if heroe['nivel'] >= 5:
                    invocaciones.append({'fila': datos['fila'], 'columna': datos['columna']})
                    mapa[datos['fila']][datos['columna']] = '🐺'
                else:
                    mapa[datos['fila']][datos['columna']] = '🌲'
                datos['vivo'] = False
                ganar_xp(50)

    # Nivel 5+: también eliminar móviles en radio de la princesa (solo horizontal y vertical)
    if heroe['nivel'] >= 5:
        for nombre_dragon, datos in dragones_moviles.items():
            if datos['vivo']:
                misma_fila = datos['fila'] == filaPrincesa and abs(datos['columna'] - columnaPrincesa) <= radio
                misma_columna = datos['columna'] == columnaPrincesa and abs(datos['fila'] - filaPrincesa) <= radio
                if misma_fila or misma_columna:
                    invocaciones.append({'fila': datos['fila'], 'columna': datos['columna']})
                    mapa[datos['fila']][datos['columna']] = '🐺'
                    datos['vivo'] = False
                    ganar_xp(50)

def movimiento_invocaciones():
    global invocaciones

    invocaciones_vivas = []
    for inv in invocaciones:
        fila, columna = inv['fila'], inv['columna']
        
        direcciones = [0, 1, 2, 3]
        random.shuffle(direcciones)
        movida = False

        for direccion in direcciones:
            if direccion == 0 and columna - 1 >= 0:
                nueva_fila, nueva_columna = fila, columna - 1
            elif direccion == 1 and columna + 1 < tamano_mapa:
                nueva_fila, nueva_columna = fila, columna + 1
            elif direccion == 2 and fila - 1 >= 0:
                nueva_fila, nueva_columna = fila - 1, columna
            elif direccion == 3 and fila + 1 < tamano_mapa:
                nueva_fila, nueva_columna = fila + 1, columna
            else:
                continue

            casilla = mapa[nueva_fila][nueva_columna]

            if casilla in (mi_personaje, '👸'):
                continue  # no puede ir a casilla del héroe ni princesa
            elif casilla in ('🐉', '🐲'):
                # mata al dragón
                if casilla == '🐲':
                    for nombre_dragon, datos in dragones_moviles.items():
                        if datos['fila'] == nueva_fila and datos['columna'] == nueva_columna:
                            datos['vivo'] = False
                            ganar_xp(50)
                            break
                else:
                    ganar_xp(10)
                mapa[fila][columna] = '🌲'
                mapa[nueva_fila][nueva_columna] = '🌲'
                movida = True
                break
            elif casilla == mi_municion:
                heroe['ataques'] += 1
                mapa[fila][columna] = '🌲'
                mapa[nueva_fila][nueva_columna] = '🌲'
                movida = True
                break
            elif casilla == '🌲':
                mapa[fila][columna] = '🌲'
                mapa[nueva_fila][nueva_columna] = '🐺'
                inv['fila'] = nueva_fila
                inv['columna'] = nueva_columna
                invocaciones_vivas.append(inv)
                movida = True
                break

        if not movida:
            # no pudo moverse, desaparece
            mapa[fila][columna] = '🌲'

    invocaciones = invocaciones_vivas

################################

lista_personajes = ('⚔️ ','🏹','🧙')

print('¡Bienvenido héroe! Debes rescatar a la princesa pasando a través de feroces dragones.')
print(lista_personajes[0],' : El caballero es un luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gastas un ataque por cada dragón derrotado.')
print(lista_personajes[1],' : El arquero es un luchador a distancia. Para atacar selecciona el botón de ataque (E).',end= ' ')
print('Solo puede atacar en la dirección del último movimiento realizado y únicamente a dos posiciones respecto a la actual.', end= ' ')
print('Si el primer movimiento es un ataque se hará hacia la derecha. El ataque se reduce aunque falles el golpe.')
print(lista_personajes[2],' : 🧙 El Mago - DLC "El Pacto del Caos". El más poderoso de los tres héroes. Ataca a distancia con E y desata una explosión caótica en área con H... pero cuidado, el poder tiene un precio.')
print('🗡️ /➶ /⚡: Recoge tu munición para recuperar 1 punto de ataque')
#######################

print('🌲', '🐉', '🐲', '⚔️ ', '🏹', '🧙', '👸', '🏰', '☠️ ', '🪦', '🗡️ ', '➶ ', '❤️')
princesa_muerta = False

nombre_personaje = input('Introduce tu nombre, héroe: ')
mi_personaje = selector_de_personaje()

mi_municion = selector_municion()
turnos_caos = 0

pantalla_actual = 1  
tamano_mapa, num_dragones, max_dragones_moviles, municion_inicial = obtener_parametros_pantalla(pantalla_actual)
    
max_municion = max_dragones_moviles // 2
max_habilidades = 1

heroe = {
    'ataques': 3,
    'habilidades_especiales': max_habilidades,
    'nivel': 1,
    'experiencia': 0,
    'escudo_activo': None,
    'radio_taunt': None,
    'distancia_disparo': None
}



if mi_personaje == '⚔️ ':
    heroe['escudo_activo'] = False
    aplicar_nivel_caballero()
elif mi_personaje in ('🏹', '🧙'):
    if mi_personaje == '🏹':
        aplicar_nivel_arquero()
        invocaciones = []
    elif mi_personaje == '🧙':
        aplicar_nivel_mago()
save = cargar_save(nombre_personaje, mi_personaje)

if save:
    nivel_guardado, pantalla_guardada, xp_guardado = save
    heroe['nivel'] = nivel_guardado
    heroe['experiencia'] = xp_guardado
    pantalla_actual = pantalla_guardada
    tamano_mapa, num_dragones, max_dragones_moviles, municion_inicial = obtener_parametros_pantalla(pantalla_actual)
    if mi_personaje == '⚔️ ':
        aplicar_nivel_caballero()
    elif mi_personaje == '🏹':
        aplicar_nivel_arquero()
        invocaciones = []
    elif mi_personaje == '🧙':
        aplicar_nivel_mago()
mapa = [['🌲'] * tamano_mapa for _ in range(tamano_mapa)]

print('####################################')
if mi_personaje == '⚔️ ':
    print(f'Bienvenido {mi_personaje} caballero {nombre_personaje}.')
    ataque_especial = 'Escudo Desafiante'
if mi_personaje == '🏹':
    print(f'Bienvenido {mi_personaje} arquero {nombre_personaje}.')
    ataque_especial = 'Disparo Invocador'
if mi_personaje == '🧙':
    print(f'Bienvenido {mi_personaje} mago {nombre_personaje}.')
    ataque_especial = 'Explosión Caótica'

print(f'Vamos a rescatar a la princesa.')

cargar_mapa()
dragones_moviles = selector_dragon_movil()
limpiar_pantalla()
mostrar_estado()
mostrar_mapa()


ultimo_movimiento = 'd' # Como dijimos que el primer ataque, si no se ha movido antes es hacia la derecha lo inicializamos
movimiento = seleccionar_movimiento()  # Primera jugada antes del bucle
if heroe['ataques'] < 0:
    heroe['ataques'] = 0

while True:

    if movimiento.lower() == 'e':
        if princesa_muerta:
            limpiar_pantalla()
            mostrar_estado('🪦 ¡Has matado a la princesa! ☠️ ¡La deshonra caera sobre ti!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        resultado_dragon = movimiento_dragon()
        if resultado_dragon == '☠️ ':
            limpiar_pantalla()
            mostrar_estado('☠️  ¡El héroe ha perdido!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        elif resultado_dragon == '🪦':
            limpiar_pantalla()
            mostrar_estado('🪦 ¡Los dragones han capturado a la princesa!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        movimiento_invocaciones()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue
    elif movimiento.lower() == 'h':
        if heroe['habilidades_especiales'] == 0:
            print('No tienes habilidades especiales disponibles')
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        habilidad_especial()
        mostrar_estado()
        mostrar_mapa()
        while input("Habilidad especial activada") != "":
            pass
        resultado_dragon = movimiento_dragon()
        if resultado_dragon == '☠️ ':
            limpiar_pantalla()
            mostrar_estado('☠️  ¡El héroe ha perdido!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        elif resultado_dragon == '🪦':
            limpiar_pantalla()
            mostrar_estado('🪦 ¡Los dragones han capturado a la princesa!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        movimiento_invocaciones()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue



    if heroe['escudo_activo']:
        resultado_dragon = movimiento_dragon()
        if resultado_dragon == '🪦':
            limpiar_pantalla()
            mostrar_estado('🪦 ¡Los dragones han capturado a la princesa!', fin_partida=True)
            mostrar_mapa()
            cargar_pantalla_derrota()
            cargar_mapa()
            dragones_moviles = selector_dragon_movil()
            limpiar_pantalla()
            mostrar_estado()
            mostrar_mapa()
            movimiento = seleccionar_movimiento()
            continue
        movimiento_invocaciones()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue

    resultado_heroe = movimiento_caballero(movimiento)
        
    
    if resultado_heroe == 'invalido':
        print('Movimiento no válido')
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue

    if resultado_heroe == '☠️ ':
        limpiar_pantalla()
        mostrar_estado('☠️  ¡El héroe ha perdido!', fin_partida=True)
        mostrar_mapa()  
        cargar_pantalla_derrota()
        cargar_mapa()
        dragones_moviles = selector_dragon_movil()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue
    elif resultado_heroe == '👸':
        mapa[tamano_mapa - 1][tamano_mapa - 1] = '🏰'
        ganar_xp(100)
        limpiar_pantalla()
        mostrar_estado('🏰  ¡La princesa ha sido rescatada!', fin_partida=True)
        mostrar_mapa()
        pantalla_actual = cargar_pantalla(pantalla_actual)
        cargar_mapa()
        dragones_moviles = selector_dragon_movil()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue
    elif resultado_heroe == '🪦':
        limpiar_pantalla()
        mostrar_estado('🪦 ¡Has matado a la princesa! ☠️ ¡La deshonra caera sobre ti!', fin_partida=True)
        mostrar_mapa()
        cargar_pantalla_derrota()
        cargar_mapa()
        dragones_moviles = selector_dragon_movil()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue      


    resultado_dragon = movimiento_dragon()
    

    if resultado_dragon == '☠️ ':
        limpiar_pantalla()
        mostrar_estado('☠️  ¡El héroe ha perdido!', fin_partida=True)
        mostrar_mapa()
        cargar_pantalla_derrota()
        cargar_mapa()
        dragones_moviles = selector_dragon_movil()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue
    elif resultado_dragon == '🪦':
        limpiar_pantalla()
        mostrar_estado('🪦 ¡Los dragones han capturado a la princesa!', fin_partida=True)
        mostrar_mapa()
        cargar_pantalla_derrota()
        cargar_mapa()
        dragones_moviles = selector_dragon_movil()
        limpiar_pantalla()
        mostrar_estado()
        mostrar_mapa()
        movimiento = seleccionar_movimiento()
        continue
    movimiento_invocaciones()
    limpiar_pantalla()
    mostrar_estado()
    mostrar_mapa()
    
    movimiento = seleccionar_movimiento()