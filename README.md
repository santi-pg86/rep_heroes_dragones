# 🐉 Rescatar a la Princesa

Juego de aventuras en consola desarrollado en Python.

## 🎮 Descripción
El héroe debe atravesar un mapa lleno de dragones para rescatar a la princesa. Elige tu personaje, introduce tu nombre y ¡a aventurarse! Cada vez que rescates a la princesa podrás avanzar a una pantalla más difícil o repetir la actual para ganar experiencia.

## 💾 Sistema de Guardado
La partida se guarda automáticamente cada vez que rescatas a la princesa (al elegir avanzar, repetir o salir) y también cuando el héroe muere o la princesa es capturada. Los datos guardados son el nivel del héroe, la XP acumulada y la pantalla actual.

Al iniciar el juego, si existe una partida guardada para ese nombre y clase de héroe, se pregunta si se desea cargar. Los ficheros de guardado se almacenan en la carpeta `saves_heroes_dragones` con el formato `<nombre>_<clase>.txt`.

## 👾 Personajes
- ⚔️ **Caballero**: luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gasta un ataque por dragón.
- 🏹 **Arquero**: luchador a distancia. Usa la tecla **E** para disparar en la dirección del último movimiento. Usa **H** para el disparo dirigido.
- 🧙 **Mago** *(DLC "El Pacto del Caos")*: el más poderoso de los tres héroes. Ataca a distancia con **E** y desata una explosión caótica en área con **H**... pero cuidado, el poder tiene un precio.

## 🗺️ Progresión de Pantallas

| Pantalla | Mapa | Dragones | Móviles | Munición |
|---|---|---|---|---|
| 1 | 5x5 | 5 | 2 | 2 |
| 2 | 10x10 | 20 | 10 | 5 |
| 3 | 15x15 | 45 | 22 | 12 |
| 4 | 20x20 | 80 | 40 | 20 |
| 5 | 25x25 | 125 | 62 | 32 |
| 6+ | 30x30 | +5% por pantalla | 50% dragones | 45 |

Al rescatar a la princesa puedes elegir avanzar a la siguiente pantalla, repetir la actual para farmear experiencia, o salir. Si pierdes, puedes reintentar la misma pantalla o salir.

## 🐲 Dragones Móviles
Además de los dragones estáticos, hay dragones móviles que se mueven por el mapa después de cada turno del héroe.

- Se mueven aleatoriamente una casilla (arriba, abajo, izquierda o derecha).
- Solo pueden moverse a casillas vacías 🌲, o hacia el héroe y la princesa.
- Si alcanzan al héroe sin ataques → el héroe muere.
- Si el caballero tiene ataques cuando coinciden → el dragón muere.
- El arquero y el mago mueren siempre al contacto con un dragón móvil.
- Si llegan a la princesa antes que el héroe → el héroe pierde.
- Al morir un dragón móvil, se selecciona un nuevo dragón estático para reemplazarlo.

## 🕹️ Controles
- **W** → Arriba
- **S** → Abajo
- **A** → Izquierda
- **D** → Derecha
- **E** → Ataque (arquero y mago). Se indica la dirección del disparo en el prompt.
- **H** → Habilidad especial

## 🛡️ Equipamiento
- 🗡️ / ➶ / ⚡: Recoge tu munición para recuperar 1 punto de ataque.

## ⚡ Habilidades Especiales

### ⚔️ Caballero - Escudo
Activa un escudo que absorbe varios impactos de dragón según el nivel. Mientras está activo:
- Los dragones móviles cercanos son atraídos hacia él (taunt).
- El caballero permanece inmóvil.
- El escudo se desactiva al absorber el número máximo de dragones del nivel.
- A partir del nivel 5, antes de activar el escudo elimina automáticamente todos los dragones estáticos en un radio de 2 casillas.

### 🏹 Arquero - Disparo dirigido
Permite seleccionar libremente la dirección del disparo, independientemente del último movimiento. Distancia mínima: 2 casillas.

**Nivel 5+:** El disparo dirigido realiza dos pasadas:
1. **Primera pasada**: mata a todos los dragones estáticos en el rango completo.
2. **Segunda pasada**: para en el primer dragón móvil encontrado en el rango.

Los dragones móviles siempre detienen la flecha; los estáticos solo la detienen por debajo del nivel 5.

### 🧙 Mago - El Pacto del Caos
Lanza un ataque en área en forma de cruz que mata a **todos** los dragones dentro del radio, sin distancia mínima. Sin embargo, durante los turnos siguientes todos los dragones móviles se dirigen directamente hacia la princesa.

**Nivel 5+:** Al activar H se aplica un bonus antes de la explosión:
- Cada dragón móvil elimina todos los dragones estáticos en un radio de `min(2 × ataques_disponibles, 10)` casillas (solo horizontal y vertical).
- Por cada 4 dragones estáticos eliminados con el bonus, se resta 1 turno de caos.
- Los ataques del mago se reducen a 0 al activar el bonus.

## 💎 Sistema de Drop
Al matar activamente a un dragón existe una probabilidad de que aparezca munición en el mapa.

- Los dragones móviles 🐲 tienen mayor probabilidad de drop que los estáticos 🐉.
- La cantidad máxima de munición en el mapa depende del número de dragones móviles vivos.

## ⭐ Sistema de XP y Niveles

| Acción | XP |
|---|---|
| Matar dragón estático 🐉 | 10 XP |
| Matar dragón móvil 🐲 | 50 XP |
| Rescatar a la princesa 👸 | 100 XP |

La experiencia y el nivel se mantienen entre pantallas. Nivel máximo: 10.

## ⚔️ Niveles del Caballero

| Nivel | Ataques | Radio taunt | Dragones absorbidos | Habilidades | Bonus |
|---|---|---|---|---|---|
| 1 | 3 | 4 | 1 | 1 | - |
| 2 | 3 | 4 | 3 | 1 | - |
| 3 | 3 | 5 | 5 | 1 | - |
| 4 | 3 | 5 | 7 | 1 | - |
| 5 | 3 | 5 | 9 | 1 | Elimina dragones estáticos en radio 2 al activar escudo |
| 6 | 4 | 5 | 9 | 2 | Elimina dragones estáticos en radio 2 al activar escudo |
| 7 | 5 | 5 | 9 | 2 | Elimina dragones estáticos en radio 2 al activar escudo |
| 8 | 6 | 5 | 9 | 3 | Elimina dragones estáticos en radio 2 al activar escudo |
| 9 | 7 | 5 | 9 | 3 | Elimina dragones estáticos en radio 2 al activar escudo |
| 10 | 8 | 5 | 9 | 3 | Elimina dragones estáticos en radio 2 al activar escudo |

## 🏹 Niveles del Arquero

| Nivel | Ataques | Dist E | Dist H | Habilidades | Bonus |
|---|---|---|---|---|---|
| 1 | 3 | 2 | 2 | 1 | - |
| 2 | 3 | 3 | 4 | 1 | - |
| 3 | 3 | 3 | 5 | 1 | - |
| 4 | 3 | 3 | 5 | 1 | - |
| 5 | 3 | 4 | 5 | 1 | La flecha mata a todos los dragones estáticos en el rango |
| 6 | 4 | 4 | 5 | 2 | La flecha mata a todos los dragones estáticos en el rango |
| 7 | 5 | 4 | 5 | 2 | La flecha mata a todos los dragones estáticos en el rango |
| 8 | 6 | 4 | 5 | 3 | La flecha mata a todos los dragones estáticos en el rango |
| 9 | 7 | 4 | 5 | 3 | La flecha mata a todos los dragones estáticos en el rango |
| 10 | 8 | 4 | 5 | 3 | La flecha mata a todos los dragones estáticos en el rango |

## 🧙 Niveles del Mago

| Nivel | Ataques | Dist E | Radio H | Habilidades | Turnos caos | Bonus |
|---|---|---|---|---|---|---|
| 1 | 3 | 2 | 2 | 1 | 3 | - |
| 2 | 3 | 3 | 3 | 1 | 3 | - |
| 3 | 3 | 3 | 4 | 1 | 3 | - |
| 4 | 3 | 3 | 4 | 1 | 3 | - |
| 5 | 3 | 4 | 5 | 1 | 3 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |
| 6 | 4 | 4 | 5 | 2 | 4 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |
| 7 | 5 | 4 | 5 | 2 | 5 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |
| 8 | 6 | 4 | 5 | 3 | 6 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |
| 9 | 7 | 4 | 5 | 3 | 7 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |
| 10 | 8 | 4 | 5 | 3 | 8 | Elimina estáticos en radio min(2×ataques,10) por cada dragón móvil |

## 📊 Panel de Estado
Antes de cada turno se muestra un panel con:
- Pantalla actual y número de dragones estáticos y móviles.
- Ataques disponibles.
- Nivel y XP actual / XP para siguiente nivel.
- Caballero: habilidad con radio taunt, dragones absorbibles, usos disponibles y bonus si nivel ≥ 5.
- Arquero: distancia ataque E, habilidad con radio H, usos disponibles y bonus si nivel ≥ 5.
- Mago: distancia ataque E, habilidad con radio H, usos disponibles, radio del bonus si nivel ≥ 5.
- Escudo activo con dragones restantes por absorber (caballero).
- Pacto del Caos activo y turnos restantes (mago).

## 🚀 Ejecución
```
python rescatar_princesa.py
```
