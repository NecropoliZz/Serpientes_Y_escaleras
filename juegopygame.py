import pygame
from datospygame import*
from bibliotecapygame import*
pygame.init()
pygame.display.set_caption("PyGame")
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
personaje = pygame.image.load("personajechibi.png").convert_alpha()
personaje = pygame.transform.scale(personaje, (90, 90))
menu = pygame.image.load("menu.png")
boton_salir = pygame.image.load("exitboton.jpg")
boton_play = pygame.image.load("botonjugar.jpg")
score_boton = pygame.image.load("scoreboton.png")
pantalla_fin_del_juego = pygame.transform.scale(pygame.image.load("findeljuego.png"),(ANCHO_VENTANA,ALTO_VENTANA))
menu = pygame.transform.scale(menu,(800,800))
boton_salir = pygame.transform.scale(boton_salir,(200,75))
rect_salir = boton_salir.get_rect()
rect_salir.x = 300
rect_salir.y = 600
boton_play = pygame.transform.scale(boton_play,(200,75))
rect_play = boton_play.get_rect()
rect_play.x = 300
rect_play.y = 400
score_boton = pygame.transform.scale(score_boton,(200,75))
rect_score = score_boton.get_rect()
rect_score.x = 300
rect_score.y = 500
puntajes_imagen = pygame.transform.scale(pygame.image.load("puntajes.png"),(ANCHO_VENTANA,ALTO_VENTANA))
tablero = pygame.image.load("tablero.png")
tablero = pygame.transform.scale(tablero,(800,600))
ingreso_rect = pygame.Rect(100, 720, 200, 30)
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pantalla_nombre and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                ingreso_nombre = ingreso_nombre[0:-1]
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if ingreso_nombre.strip() != "":
                    nombre_jugador = ingreso_nombre.strip()
                    pantalla_nombre = False
                    estado_menu = True
            else:
                ingreso_nombre += event.unicode
        if estado_menu and event.type == pygame.MOUSEBUTTONDOWN:
            if rect_salir.collidepoint(event.pos):
                running = False
            elif rect_play.collidepoint(event.pos):
                estado_menu = False
                jugando = True
                pregunta_actual = generar_pregunta_aleatoria(copia_preguntas)
            elif rect_score.collidepoint(event.pos):
                estado_menu = False
                pantalla_puntaje = True
        if jugando and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                ingreso = ingreso[0:-1]
            else:
                ingreso += event.unicode
            if event.key == pygame.K_ESCAPE:
                estado_menu = True
                jugando = False
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if pregunta_actual is not None and ingreso.strip() != "":
                    respuesta_limpia = ingreso.strip().lower()
                    es_correcta = comprobar_respuesta_correcta(pregunta_actual, key_respuesta_correcta, respuesta_limpia)
                    posicion_jugador = mover(posicion_jugador,es_correcta,Array_tablero)
                    tiempo_restante = 60
                    ingreso = ""
                    pregunta_actual = generar_pregunta_aleatoria(copia_preguntas)
        if jugando and event.type == pygame.USEREVENT:
            if event.type == timer_segundos:
                tiempo_restante -= 1
                if tiempo_restante <= 0:
                    es_correcta = False
                    posicion_jugador = mover(posicion_jugador,es_correcta,Array_tablero)
                    tiempo_restante = 60
                    ingreso = ""
                    pregunta_actual = generar_pregunta_aleatoria(copia_preguntas)
    pantalla.fill(NEGRO)
    if pantalla_nombre:
        font = pygame.font.SysFont("Arial", 36)
        font_pequeña = pygame.font.SysFont("Arial", 20)
        # Titulo
        titulo = font.render("¡Bienvenido al juego!", True, BLANCO)
        titulo_rect = titulo.get_rect(center=(ANCHO_VENTANA//2, 250))
        pantalla.blit(titulo, titulo_rect)
        # Instrucciones
        instrucciones = font_pequeña.render("Ingresa tu nombre:", True, BLANCO)
        instrucciones_rect = instrucciones.get_rect(center=(ANCHO_VENTANA//2, 350))
        pantalla.blit(instrucciones, instrucciones_rect)
        # Campo de entrada
        input_rect = pygame.Rect(ANCHO_VENTANA//2 - 150, 400, 300, 50)
        pygame.draw.rect(pantalla, BLANCO, input_rect, 2)
        pygame.draw.rect(pantalla, BLANCO, input_rect, 2)
        # Texto del nombre
        texto_nombre = font_pequeña.render(ingreso_nombre, True, BLANCO)
        pantalla.blit(texto_nombre, (input_rect.x + 10, input_rect.y + 15))
    if estado_menu:
        mostrar_menu(pantalla,menu,boton_play,score_boton,boton_salir)
    elif jugando:
        pantalla.blit(tablero, (0,0))
        pantalla.blit(personaje,coordenadas_casillas[posicion_jugador])
        font = pygame.font.SysFont("Arial", 15)
        texto = font.render("Presiona ESC para volver al menú", True, BLANCO)
        pantalla.blit(texto, (500, 750))
        texto_tiempo = font.render(f"Tiempo: {tiempo_restante}s", True, BLANCO)
        pantalla.blit(texto_tiempo, (700, 700))
        if pregunta_actual is not None:
            texto_instrucciones = font.render("Escribe a, b o c y presiona ENTER para responder", True, BLANCO)
            pantalla.blit(texto_instrucciones, (50, 760))
            pygame.draw.rect(pantalla, BLANCO, ingreso_rect, 2)
            texto_respuesta = font.render(f"Tu respuesta: {ingreso}", True, BLANCO)
            pantalla.blit(texto_respuesta, (ingreso_rect.x + 5, ingreso_rect.y + 5))
            mostrar_pregunta(pantalla, pregunta_actual, 50, 600, "Arial", BLANCO)
        else:
            texto_fin = font.render("¡Se acabaron las preguntas!", True, BLANCO)
            pantalla.blit(texto_fin, (300, 650))
    if pantalla_puntaje:
        pantalla.blit(puntajes_imagen,(0,0))
        scores = leer_archivo()
        ordenar_scores(scores)
        puntajes_renderizados = renderizar_puntajes(scores,"Arial",NEGRO)
        mostrar_puntajes(pantalla,puntajes_renderizados)
    pygame.display.flip()          
pygame.quit()