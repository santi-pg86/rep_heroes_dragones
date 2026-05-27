# 🐉 Rescatar a la Princesa

Juego de aventuras en consola desarrollado en Python.

## 🎮 Descripción
El héroe debe atravesar un mapa lleno de dragones para rescatar a la princesa. Elige tu personaje, introduce tu nombre y ¡a aventurarse! Cada vez que rescates a la princesa podrás avanzar a una pantalla más difícil o repetir la actual para ganar experiencia.

## 💾 Sistema de Guardado
La partida se guarda automáticamente cada vez que rescatas a la princesa (al elegir avanzar, repetir o salir) y también cuando el héroe muere o la princesa es capturada. Los datos guardados son el nivel del héroe, la XP acumulada y la pantalla actual.

Al iniciar el juego, si existe una partida guardada para ese nombre y clase de héroe, se pregunta si se desea cargar. Los ficheros de guardado se almacenan en la carpeta `saves_heroes_dragones` con el formato `<nombre>_<clase>.txt`.

## 👾 Personajes
- ⚔️ **Caballero**: luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gasta un ataque por dragón.
- 🏹 **Arquero**: luchador a distancia. Usa la tecla **E** para disparar en la dirección del último movimiento. Usa **H** para invocar lobos aliados.
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

### ⚔️ Caballero - Escudo Desafiante
Activa un escudo que absorbe varios impactos de dragón según el nivel. Mientras está activo:
- Los dragones móviles cercanos son atraídos hacia él (taunt).
- El caballero permanece inmóvil.
- El escudo se desactiva al absorber el número máximo de dragones del nivel.
- El escudo también se desactiva automáticamente si no quedan dragones móviles en el mapa.
- **Nivel 5+**: antes de activar el escudo elimina automáticamente los dragones estáticos en un radio de `min(ataques, 10)` casillas (horizontal y vertical). Por cada estático eliminado, el escudo puede absorber 1 dragón adicional.

### 🏹 Arquero - Disparo Invocador
Elimina los dragones móviles que estén en la misma fila o columna del héroe dentro del radio de la habilidad.

**Nivel 5+:** Además elimina los dragones móviles en la misma fila o columna de la princesa, e invoca un 🐺 lobo en cada casilla liberada. Los lobos se mueven aleatoriamente cada turno y:
- Al encontrar un dragón (estático o móvil) → ambos mueren, el héroe gana XP.
- Al encontrar munición → +1 ataque al héroe, el lobo desaparece.
- Si no pueden moverse → desaparecen.
- No pueden moverse a la casilla del héroe ni de la princesa.
- Un lobo aliado bloquea el paso del héroe.

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
| 5 | 3 | 5 | 9 | 1 | Radio min(ataques,10), +1 absorbible por estático eliminado |
| 6 | 4 | 5 | 9 | 2 | Radio min(ataques,10), +1 absorbible por estático eliminado |
| 7 | 5 | 5 | 9 | 2 | Radio min(ataques,10), +1 absorbible por estático eliminado |
| 8 | 6 | 5 | 9 | 3 | Radio min(ataques,10), +1 absorbible por estático eliminado |
| 9 | 7 | 5 | 9 | 3 | Radio min(ataques,10), +1 absorbible por estático eliminado |
| 10 | 8 | 5 | 9 | 3 | Radio min(ataques,10), +1 absorbible por estático eliminado |

## 🏹 Niveles del Arquero

| Nivel | Ataques | Dist E | Dist H | Habilidades | Bonus |
|---|---|---|---|---|---|
| 1 | 3 | 3 | 3 | 1 | - |
| 2 | 3 | 3 | 3 | 1 | - |
| 3 | 3 | 4 | 4 | 1 | - |
| 4 | 3 | 4 | 4 | 1 | - |
| 5 | 3 | 5 | 5 | 1 | Invoca 🐺 lobos también en radio de la princesa |
| 6 | 4 | 6 | 6 | 2 | Invoca 🐺 lobos también en radio de la princesa |
| 7 | 5 | 7 | 7 | 2 | Invoca 🐺 lobos también en radio de la princesa |
| 8 | 6 | 8 | 8 | 3 | Invoca 🐺 lobos también en radio de la princesa |
| 9 | 7 | 9 | 9 | 3 | Invoca 🐺 lobos también en radio de la princesa |
| 10 | 8 | 10 | 10 | 3 | Invoca 🐺 lobos también en radio de la princesa |

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

## 📄 Licencia
Copyright (C) 2026 Santiago Pérez García

Este programa se distribuye bajo la licencia **GNU General Public License v3.0**.
Ver el fichero [LICENSE](LICENSE) para más detalles.

## 🚀 Ejecución
```
python rescatar_princesa.py
```
