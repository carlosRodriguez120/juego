import pygame

# inicializar pygame
pygame.init()

# crear la pantalla ancho x alto
pantalla = pygame.display.set_mode((800, 600))

# titulo de la pantalla +ICONO
pygame.display.set_caption("INVASION ESPACIL")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)


# crear el personaje+ variables del jugador

imgJugador = pygame.image.load("nave.png")
jugadorX = 368
jugadorY = 536
jugadorX_cambio = 0
jugadorY_cambio = 0
# crear al enemigo

imgEnemigo = pygame.image.load("astronave.png")
enemigoX = 368
enemigoY = 100
enemigoX_cambio = 0
enemigoY_cambio = 0

def jugador(x, y):
    pantalla.blit(imgJugador, (x, y))

def enemigo(x, y):
    pantalla.blit(imgEnemigo, (x, y))

# loop para programar los eventos
se_ejecuta = True
while se_ejecuta:
    # cambiamos el color de fondo en la pantalla
    # se tiene que actualizar con el .display
    pantalla.fill((48, 32, 139))
    #evento para salir de la pantalla usando QUIT

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento para insertar movimiento al personaje cuando presionamos las flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorX_cambio = -0.2
                
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0.2
                
            if evento.key == pygame.K_UP:
                jugadorY_cambio = -0.2
            if evento.key == pygame.K_DOWN:
                jugadorY_cambio = 0.2
        # evento para detener el movimiento cuando soltamos las flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                jugadorX_cambio = 0
                jugadorY_cambio = 0
     #asignamos el valor de movimiento a las variables del jugador           
    jugadorX += jugadorX_cambio
    jugadorY += jugadorY_cambio



    # mantener dentro de bordes 
    if jugadorX<=0:
        jugadorX=0
    elif jugadorX>=736:
        jugadorX=736
    elif jugadorY<=0:
        jugadorY=0
    elif jugadorY>=540:
        jugadorY=540
        


    jugador(jugadorX, jugadorY)
    enemigo(enemigoX,enemigoY)
    # actualizar
    pygame.display.update()
