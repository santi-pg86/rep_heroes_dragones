# 🐉 Rescatar a la Princesa

Juego de aventuras en consola desarrollado en Python.

## 🎮 Descripción
El héroe debe atravesar un mapa lleno de dragones para rescatar a la princesa. 
Elige tu personaje, selecciona la dificultad y ¡a aventurarse!

## 👾 Personajes
- ⚔️ **Caballero**: luchador cuerpo a cuerpo. Pasa por encima de un dragón para derrotarlo. Gasta un ataque por dragón.
- 🏹 **Arquero**: luchador a distancia. Usa la tecla **E** para disparar dos casillas en la dirección del último movimiento. Gasta un ataque aunque falle.
- 🧙 **Mago**: bloqueado. Compra el DLC para desbloquearlo.

## 🗺️ Dificultad
| Nivel | Mapa | Dragones | Munición inicial | Dragones móviles |
|---|---|---|---|---|
| 0 - Fácil | 5x5 | 5 | 1 | 1 |
| 1 - Media | 10x10 | 10 | 3 | 2 |

## 🐲 Dragones Móviles
Además de los dragones estáticos, hay dragones móviles que se mueven por el mapa después de cada turno del héroe.

- Se mueven aleatoriamente una casilla (arriba, abajo, izquierda o derecha).
- Solo pueden moverse a casillas vacías 🌲, o hacia el héroe y la princesa.
- Si el caballero tiene ataques cuando coinciden → el dragón muere.
- El arquero muere siempre al contacto con un dragón móvil.
- Si llegan a la princesa antes que el héroe → el héroe pierde.
- Al morir un dragón móvil, se selecciona un nuevo dragón estático para reemplazarlo.

## 🕹️ Controles
- **W** → Arriba
- **S** → Abajo
- **A** → Izquierda
- **D** → Derecha
- **E** → Ataque (solo arquero)

## 🛡️ Equipamiento
- 🗡️ **Caballero**: recoge espadas para recuperar 1 ataque.
- ➶ **Arquero**: recoge flechas para recuperar 1 ataque.

## 💎 Sistema de Drop
Al matar activamente a un dragón existe una probabilidad de que aparezca munición en el mapa.

- Los dragones móviles 🐲 tienen mayor probabilidad de drop que los estáticos 🐉.
- La cantidad máxima de munición en el mapa depende del número de dragones móviles vivos.

## 🚀 Ejecución
```
python rescatar_princesa.py
```
