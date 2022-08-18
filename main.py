import random
import pygame

# inicializar pygame
pygame.init()

# crear la pantalla ancho x alto
pantalla = pygame.display.set_mode((800, 600))

# titulo de la pantalla +ICONO
pygame.display.set_caption("INVASION ESPACIL")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

# crear el personaje+ variables del jugador

imgJugador = pygame.image.load("nave.png")
jugadorX = 368
jugadorY = 536
jugadorX_cambio = 0
jugadorY_cambio = 0

# crear al enemigo

imgEnemigo = pygame.image.load("astronave.png")
enemigoX = random.randint(0,736)
enemigoY = random.randint(0,100)
enemigoX_cambio = 0.3
enemigoY_cambio = 30

# variables de la bala

imgBala = pygame.image.load("balas.png")
balaX = 0
balaY = 0
balaX_cambio = 0
balaY_cambio = 1
balaVisible = False

def jugador(x, y):
    pantalla.blit(imgJugador, (x, y))

def enemigo(x, y):
    pantalla.blit(imgEnemigo, (x, y))

def dispararBala(x,y):
    global balaVisible
    balaVisible = True
    pantalla.blit(imgBala, (x,y+10))


# loop para programar los eventos
se_ejecuta = True
while se_ejecuta:
    # cambiamos el color de fondo en la pantalla
    # se tiene que actualizar con el .display
    pantalla.blit(fondo,(0,0))
    #evento para salir de la pantalla usando QUIT

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento para insertar movimiento al personaje cuando presionamos las flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorX_cambio = -0.5
                
            if evento.key == pygame.K_RIGHT:
                jugadorX_cambio = 0.5
                
            if evento.key == pygame.K_UP:
                jugadorY_cambio = -0.5
            if evento.key == pygame.K_DOWN:
                jugadorY_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                dispararBala(jugadorX,balaY)


        # evento para detener el movimiento cuando soltamos las flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                jugadorX_cambio = 0
                jugadorY_cambio = 0
     #asignamos el valor de movimiento a las variables del jugador           
    jugadorX += jugadorX_cambio
    jugadorY += jugadorY_cambio



    # mantener dentro de bordes al jugador

    if jugadorX<=0:
        jugadorX=0
    elif jugadorX>=736:
        jugadorX=736
    elif jugadorY<=0:
        jugadorY=0
    elif jugadorY>=540:
        jugadorY=540
    

     #asignamos el valor de movimiento a las variables del enemigo  

    enemigoX+=enemigoX_cambio

        # mantener dentro de bordes al enemigo

    if enemigoX<=0:
        enemigoX_cambio=0.3
        enemigoY += enemigoY_cambio
    elif enemigoX>=736:
        enemigoX_cambio=-0.3
        enemigoY += enemigoY_cambio

    #MOVIMIENTO BALA
   
    if balaVisible :
        balaY=jugadorY
        dispararBala(jugadorX,balaY) 
        balaY -=balaY_cambio
        


    jugador(jugadorX, jugadorY)
    enemigo(enemigoX,enemigoY)
    # actualizar
    pygame.display.update()
