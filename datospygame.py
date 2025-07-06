import copy
running = True
pantalla_nombre = True
posicion_jugador = 15
tiempo_restante = 60
estado_menu = False
jugando = False
pantalla_puntaje = False
ALTO_VENTANA = 800
ANCHO_VENTANA = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
nombre_jugador = ""  
ingreso_nombre = "" 
ingreso = ""
Array_tablero = [0,1,0,0,0,3,0,0,0,0,0,1,0,0,2,0,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0]
key_respuesta_correcta = "respuesta_correcta"
preguntas = [
    {
        "pregunta": "¿Cuál es el país más grande del mundo por superficie?",
        "respuesta_a": "Canadá",
        "respuesta_b": "China",
        "respuesta_c": "Rusia",
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Cuál es el órgano más grande del cuerpo humano?",
        "respuesta_a": "El hígado",
        "respuesta_b": "La piel",
        "respuesta_c": "El intestino delgado",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Quién escribió Cien años de soledad?",
        "respuesta_a": "Gabriel García Márquez",
        "respuesta_b": "Mario Vargas Llosa",
        "respuesta_c": "Pablo Neruda",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es el elemento químico con símbolo O?",
        "respuesta_a": "Oro",
        "respuesta_b": "Oxígeno",
        "respuesta_c": "Osmio",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿En qué continente se encuentra Egipto?",
        "respuesta_a": "África",
        "respuesta_b": "Asia",
        "respuesta_c": "Europa",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuántos jugadores conforman un equipo de fútbol en el campo?",
        "respuesta_a": "9",
        "respuesta_b": "10",
        "respuesta_c": "11",
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Cuál es la capital de Australia?",
        "respuesta_a": "Sídney",
        "respuesta_b": "Canberra",
        "respuesta_c": "Melbourne",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Qué planeta es conocido como el 'planeta rojo'?",
        "respuesta_a": "Marte",
        "respuesta_b": "Júpiter",
        "respuesta_c": "Venus",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Quién pintó La última cena?",
        "respuesta_a": "Miguel Ángel",
        "respuesta_b": "Leonardo da Vinci",
        "respuesta_c": "Rafael",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cuál es el idioma más hablado del mundo por número de hablantes nativos?",
        "respuesta_a": "Inglés",
        "respuesta_b": "Chino mandarín",
        "respuesta_c": "Español",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cuánto es 25 x 4?",
        "respuesta_a": "100",
        "respuesta_b": "75",
        "respuesta_c": "90",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Si tienes 3 docenas de huevos, cuántos huevos tienes?",
        "respuesta_a": "36",
        "respuesta_b": "30",
        "respuesta_c": "24",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cuál es el resultado de 120 ÷ 10?",
        "respuesta_a": "10",
        "respuesta_b": "12",
        "respuesta_c": "14",
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cuánto es 7 x 8?",
        "respuesta_a": "56",
        "respuesta_b": "48",
        "respuesta_c": "64",
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "Si tienes $50 y gastas $18, ¿cuánto te queda?",
        "respuesta_a": "$32",
        "respuesta_b": "$28",
        "respuesta_c": "$38",
        "respuesta_correcta": "a"
    }
]
copia_preguntas = copy.deepcopy(preguntas)
coordenadas_casillas = [
    # Casilla 0 (X - posición inicial fuera del tablero)
    (10, 500),
    # Fila inferior (casillas 1-6): de izquierda a derecha
    (120, 500),  # 1
    (240, 500),  # 2
    (350, 500),  # 3
    (460, 500),  # 4
    (570, 500),  # 5
    (680, 500),  # 6
    # Fila 2 (casillas 7-12): de derecha a izquierda
    (575, 380),  # 7
    (450, 380),  # 8
    (350, 380),  # 9
    (225, 380),  # 10
    (125, 380),  # 11
    (10, 380),  # 12
    # Fila 3 (casillas 13-18): de izquierda a derecha
    (120, 265),  # 13
    (230, 265),  # 14
    (350, 265),  # 15
    (450, 265),  # 16
    (570, 265),  # 17
    (680, 265),  # 18
    # Fila 4 (casillas 19-24): de derecha a izquierda
    (570, 150),  # 19
    (450, 150),  # 20
    (350, 150),  # 21
    (230, 150),  # 22
    (120, 150),  # 23
    (10, 150),  # 24
    # Fila 5 (casillas 25-30): de izquierda a derecha
    (120, 30),  # 25
    (230, 30),  # 26
    (350, 30),  # 27
    (450, 30),  # 28
    (570, 30),  # 29
    (670, 30),  # 30 (meta con trofeo)
]