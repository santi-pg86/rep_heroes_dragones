# 🐉 Rescatar a la Princesa

Juego de aventuras en consola desarrollado en Python.

## 🎮 Descripción
El héroe debe atravesar un mapa lleno de dragones para rescatar a la princesa. Elige tu personaje, introduce tu nombre y ¡a aventurarse! Cada vez que rescates a la princesa podrás avanzar a una pantalla más difícil o repetir la actual para ganar experiencia.

## 👾 Personajes
- ⚔️ **Caballero**: luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gasta un ataque por dragón.
- 🏹 **Arquero**: luchador a distancia. Usa la tecla **E** para disparar dos casillas en la dirección del último movimiento. Gasta un ataque aunque falle.
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
- **E** → Ataque (arquero y mago)
- **H** → Habilidad especial

## 🛡️ Equipamiento
- 🗡️ / ➶ / ⚡: Recoge tu munición para recuperar 1 punto de ataque.

## ⚡ Habilidades Especiales

### ⚔️ Caballero - Escudo
Activa un escudo que lo hace inmune al siguiente ataque de dragón. Mientras está activo:
- Los dragones móviles cercanos son atraídos hacia él (taunt, radio 4).
- El caballero permanece inmóvil.
- El escudo se desactiva al matar al primer dragón que llega.

### 🏹 Arquero - Disparo dirigido
Permite seleccionar libremente la dirección del disparo, independientemente del último movimiento. La flecha viaja en línea recta hasta impactar con el primer dragón en su camino o alcanzar la distancia máxima. Distancia mínima: 2 casillas.

### 🧙 Mago - El Pacto del Caos
Lanza un ataque en área en forma de cruz que mata a **todos** los dragones dentro del radio, sin distancia mínima. Sin embargo, durante los **3 turnos siguientes** todos los dragones móviles se dirigen directamente hacia la princesa. Úsalo con cabeza... o perderás todo lo que acabas de ganar.

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

La experiencia y el nivel se mantienen entre pantallas. Repite pantallas para farmear XP antes de avanzar.

## 📊 Panel de Estado
Antes de cada turno se muestra un panel con:
- Pantalla actual y número de dragones estáticos y móviles.
- Ataques disponibles.
- Nivel y XP actual / XP para siguiente nivel.
- Habilidad especial disponible con radio de acción.
- Escudo activo (caballero).
- Pacto del Caos activo y turnos restantes (mago).

## 🚀 Ejecución
```
python rescatar_princesa.py
```
