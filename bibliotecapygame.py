import pygame
def mostrar_pregunta(pantalla, pregunta: dict, x: int, y: int, fuente:str, color_texto: list):
    """
    Muestra los values de pregunta en la pantalla usando pygame.font
    
    Parámetros:
    pantalla: Surface de pygame donde se va a dibujar
    pregunta(dict): Diccionario que contiene la pregunta, las opciones de respuesta y la respuesta correcta
    x(int): Posición x donde comenzar a dibujar
    y(int): Posición y donde comenzar a dibujar
    fuente: Font de pygame
    color_texto(tuple): Color del texto en formato RGB (default: blanco)
    """
    fuente = pygame.font.SysFont(fuente, 15)
    texto_pregunta = fuente.render(f"Pregunta: {pregunta['pregunta']}", True, color_texto)
    texto_a = fuente.render(f"a: {pregunta['respuesta_a']}", True, color_texto)
    texto_b = fuente.render(f"b: {pregunta['respuesta_b']}", True, color_texto)
    texto_c = fuente.render(f"c: {pregunta['respuesta_c']}", True, color_texto)
    
    altura_linea = fuente.get_height() + 10  
    
    # Dibujar los textos en pantalla
    pantalla.blit(texto_pregunta, (x, y))
    pantalla.blit(texto_a, (x, y + altura_linea))
    pantalla.blit(texto_b, (x, y + altura_linea * 2))
    pantalla.blit(texto_c, (x, y + altura_linea * 3))
def generar_pregunta_aleatoria(preguntas:list)->any:
    """
    Genera una pregunta aleatoria
    Parametros:
    preguntas(list): Lista de preguntas
    Retorno:
    Retorna un diccionario(una pregunta) en caso de que aun haya elementos en indices, caso contrario retornara None
    """
    import random
    retorno = None
    if len(preguntas) > 0:
        retorno = random.choice(preguntas)
        preguntas.remove(retorno)
    return retorno
def comprobar_respuesta_correcta(pregunta:dict,key:str,respuesta:str)->bool:
    """
    Comprueba que el value de un diccionario coincida con el dato que le estamos pasando
    Parametros:
    Pregunta(dict): Diccionario donde esta el value que queremos
    Key(str): Key para acceder al value
    respuesta(str): dato que vamos a comparar con el value del dict
    retorno: en caso de que el value y el dato no coincidan retornara False, caso contrario retornara True
    """
    retorno = False
    if pregunta[key] == respuesta:
        retorno = True
    return retorno
def mover(posicion_jugador:int,respuesta_correcta:bool,tablero:list)->int:
    """Mueve al usuario dependiendo de si respondio bien la pregunta o no"""
    casilla = 1
    if not respuesta_correcta:
        casilla = -1
    posicion_jugador += casilla
    while tablero[posicion_jugador] != 0:
        posicion_jugador += tablero[posicion_jugador]*casilla
    return posicion_jugador
def leer_archivo()->list:
    """Funcion para leer el archivo score.csv y guardar el nombre y el score"""
    scores = []
    with open("score.csv","r") as archivo:
        for linea in archivo:
            datos = linea.split(",")
            nombre = datos[0]
            score = int(datos[1])
            scores.append([nombre,score])
    return scores
def ordenar_scores(scores:list):
    """Ordena la lista de scores de manera descendente"""
    for i in range(len(scores)-1):
        for j in range(i+1,len(scores)):
            if scores[i][1] < scores[j][1]:
                aux = scores[i]
                scores[i] = scores[j]
                scores[j] = aux
def mostrar_menu(pantalla,menu,boton_play,score_boton,boton_salir):
    pantalla.blit(menu, (0, 0))
    pantalla.blit(boton_play, (300, 400))
    pantalla.blit(score_boton, (300, 500))
    pantalla.blit(boton_salir, (300, 600))
def renderizar_puntajes(scores: list, fuente: str, color_texto: tuple) -> list:
    """
    Renderiza los nombres y puntajes de la lista usando pygame.font
    
    Parámetros:
    scores(list): Lista de puntajes [nombre, puntaje]
    fuente(str): Nombre de la fuente
    color_texto(tuple): Color del texto en formato RGB
    
    Retorno:
    Lista de tuplas con las superficies renderizadas [(texto_nombre, texto_puntaje), ...]
    """
    fuente_pygame = pygame.font.SysFont(fuente, 24)
    textos_renderizados = []
    # Limitar a máximo 10 puntajes
    scores_limitados = scores[:10]
    for nombre, puntaje in scores_limitados:
        texto_nombre = fuente_pygame.render(nombre, True, color_texto)
        texto_puntaje = fuente_pygame.render(str(puntaje), True, color_texto)
        textos_renderizados.append((texto_nombre, texto_puntaje))
    return textos_renderizados
def mostrar_puntajes(pantalla, textos_renderizados: list):
    """
    Muestra los puntajes renderizados en la pantalla sobre la imagen de puntajes
    
    Parámetros:
    pantalla: Surface de pygame donde se va a dibujar
    textos_renderizados(list): Lista de tuplas con textos renderizados
    """
    # Coordenadas iniciales basadas en la imagen de 800x800
    x_nombre = 100  # Columna de nombres
    x_puntaje = 410  # Columna de puntajes
    y_actual = 140  # Fila inicial después del encabezado
    altura_fila = 70  # Espaciado entre filas
    for texto_nombre, texto_puntaje in textos_renderizados:
        # Dibujar nombre y puntaje en sus respectivas columnas
        pantalla.blit(texto_nombre, (x_nombre, y_actual))
        pantalla.blit(texto_puntaje, (x_puntaje, y_actual))
        y_actual += altura_fila