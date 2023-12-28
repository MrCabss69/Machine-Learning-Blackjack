# Redes Neurales y Algoritmos Genéticos para el Blackjack

En este proyecto se explora la resolución del juego de Blackjack utilizando una combinación de algoritmos genéticos y redes neuronales. Discutimos varias arquitecturas de redes neuronales, incluyendo CNNs y su aplicación para interpretar el estado del juego. También se considerará el uso de técnicas de aprendizaje por refuerzo y simulaciones de Montecarlo para evaluar y ajustar las decisiones de juego.



## Estructura del Proyecto

La estructura del proyecto se organiza en módulos dedicados a aspectos específicos como la lógica del juego y los algoritmos de aprendizaje automático.

```bash
BlackJack - Genetic Algorithms
.
├── core
│   ├── agenetico.py
│   ├── __init__.py
│   ├── montecarlo.py
│   └── networks.py
├── example.ipynb
├── juego
│   ├── __init__.py
│   └── juego.py
├── README.md
└── tests
    ├── auto_exec.sh
    ├── test_01_aux.py
    ├── test_02_jugador.py
    ├── test_03_estado.py
    └── test_04_juego.py
```


## Aspectos técnicos

### Algoritmos Genéticos y Redes Neuronales

Se explora la sinergia entre algoritmos genéticos y diferentes arquitecturas de redes neuronales para optimizar estrategias en Blackjack. Los algoritmos genéticos ayudan a afinar los parámetros de la red, mejorando la capacidad de decisión basada en patrones complejos del juego.

### Aprendizaje por Refuerzo y Montecarlo

Se plantea el uso de aprendizaje por refuerzo y simulaciones de Montecarlo para evaluar estrategias y tomar decisiones. Estas técnicas permiten una comprensión más profunda de las consecuencias a largo plazo de las acciones, crucial en juegos con elementos de azar como el Blackjack.

### Arquitecturas de Red Neuronal

Se consideraron varias arquitecturas, incluyendo CNNs para interpretar el estado del juego. Estas redes pueden procesar efectivamente las disposiciones de las cartas y las relaciones entre ellas, lo que es esencial en el Blackjack.