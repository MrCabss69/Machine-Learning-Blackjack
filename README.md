# Redes Neurales y Algoritmos Genéticos para el Blackjack

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
En este proyecto se explora la resolución del juego de Blackjack utilizando una combinación de algoritmos genéticos y redes neuronales. Discutimos varias arquitecturas de redes neuronales, incluyendo CNNs y su aplicación para interpretar el estado del juego. También se considerará el uso de técnicas de aprendizaje por refuerzo y simulaciones de Montecarlo para evaluar y ajustar las decisiones de juego.



## Estructura del Proyecto
<<<<<<< HEAD
=======
=======
En este proyecto se explora la resolución del juego de Blackjack utilizando una combinación de redes neuronales y algoritmos genéticos. También se considerará el uso de técnicas de aprendizaje por refuerzo y simulaciones de Montecarlo para evaluar y ajustar las decisiones de juego.

## IDEA
El juego enfrenta a un jugador contra un crupier, utilizando simulaciones de Montecarlo para analizar la dinámica del juego. Se busca establecer una relación funcional entre el estado del juego y el resultado numérico de la ronda, esencialmente modelando el problema como una tarea de clasificación multiclase con tres posibles resultados (-1, 0, 1). La función objetivo es: f(estado, acción) = resultado.

```text
Mano Jugador, Mano Crupier, Accion, Resultado

"[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]","[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]","[0, 1]",-1

"[0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]","[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]","[0, 1]",-1
```
## ESTRUCTURA DEL PROYECTO
>>>>>>> 5bc4853 (refactor on Neural Nets)
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)

La estructura del proyecto se organiza en módulos dedicados a aspectos específicos como la lógica del juego y los algoritmos de aprendizaje automático.

```bash
BlackJack - Genetic Algorithms
<<<<<<< HEAD
.
=======
<<<<<<< HEAD
.
=======
>>>>>>> 5bc4853 (refactor on Neural Nets)
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
├── core
│   ├── agenetico.py
│   ├── __init__.py
│   ├── montecarlo.py
│   └── networks.py
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
├── example.ipynb
├── juego
│   ├── __init__.py
│   └── juego.py
├── README.md
<<<<<<< HEAD
=======
=======
├── juego
│   ├── estado.py
│   ├── __init__.py
│   └── jugador.py
├── mc_1000.csv
├── mc_simulation_data.ipynb
├── model_training.ipynb
├── README.md
├── resultados_blackjack.csv
>>>>>>> 5bc4853 (refactor on Neural Nets)
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
└── tests
    ├── auto_exec.sh
    ├── test_01_aux.py
    ├── test_02_jugador.py
    ├── test_03_estado.py
    └── test_04_juego.py
```


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
## Aspectos técnicos

### Algoritmos Genéticos y Redes Neuronales

Se explora la sinergia entre algoritmos genéticos y diferentes arquitecturas de redes neuronales para optimizar estrategias en Blackjack. Los algoritmos genéticos ayudan a afinar los parámetros de la red, mejorando la capacidad de decisión basada en patrones complejos del juego.

### Aprendizaje por Refuerzo y Montecarlo

Se plantea el uso de aprendizaje por refuerzo y simulaciones de Montecarlo para evaluar estrategias y tomar decisiones. Estas técnicas permiten una comprensión más profunda de las consecuencias a largo plazo de las acciones, crucial en juegos con elementos de azar como el Blackjack.

### Arquitecturas de Red Neuronal

<<<<<<< HEAD
Se consideraron varias arquitecturas, incluyendo CNNs para interpretar el estado del juego. Estas redes pueden procesar efectivamente las disposiciones de las cartas y las relaciones entre ellas, lo que es esencial en el Blackjack.
=======
Se consideraron varias arquitecturas, incluyendo CNNs para interpretar el estado del juego. Estas redes pueden procesar efectivamente las disposiciones de las cartas y las relaciones entre ellas, lo que es esencial en el Blackjack.
=======
## ASPECTOS TÉCNICOS

### Simulaciones de Montecarlo

Las simulaciones de Montecarlo proporcionan un método robusto para evaluar diversas estrategias y decisiones en el contexto del juego. Estas simulaciones permiten la estimación del valor esperado a largo plazo de las acciones y estrategias, facilitando la identificación de las más prometedoras.


### Arquitecturas de Red Neuronal

Se exploran distintas arquitecturas de red neuronal para procesar y entender el estado del juego, y predecir el resultado de las acciones. Estas arquitecturas están diseñadas para capturar las complejas relaciones y patrones en las configuraciones de cartas, un elemento clave en la estrategia del Blackjack.


### Algoritmos Genéticos

Los algoritmos genéticos se utilizan para optimizar parámetros y estrategias de juego. Estos algoritmos simulan la evolución natural para iterativamente mejorar las decisiones de juego, ajustando las estrategias basadas en el rendimiento pasado.
>>>>>>> 5bc4853 (refactor on Neural Nets)
>>>>>>> 5e42a24 (Guardando mis cambios en una nueva rama)
