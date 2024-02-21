import pygame
import sys
import random



#ventana
ancho=800
alto=600
negro=(0,0,0)
ventana=pygame.display.set_mode((ancho, alto))
game_over=False
tiempo=pygame.time.Clock()



#jugador
tamano_jugador=50
posicion_jugador=[ancho/2,alto-tamano_jugador*2]
color_jugador=(255,0,0)


#enemigos
tamano_enemigo=50
posicion_enemigo=[random.randint(0,ancho-tamano_enemigo),0]
color_enemigo=(0,0,255)

#funciones
def detecta_colision(posicion_jugador, posicion_enemigo):
    jugador_en_x=posicion_jugador[0]
    jugador_en_y=posicion_jugador[1]
    enemigo_x=posicion_enemigo[0]
    enemigo_y=posicion_enemigo[1]

    if(enemigo_x>=jugador_en_x and enemigo_x < (jugador_en_x + tamano_jugador)) or (jugador_en_x >= enemigo_x and jugador_en_x < (enemigo_x + tamano_enemigo)):
        if(enemigo_y >= jugador_en_y and enemigo_y < (jugador_en_y + tamano_jugador)) or(jugador_en_y >= enemigo_x and jugador_en_y<(enemigo_y + tamano_jugador)):
            return True
    return False

       

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.enemigo_xit()
        if event.type==pygame.KEYDOWN:
            x=posicion_jugador[0]
            if event.key==pygame.K_LEFT:
                x-=tamano_jugador
            posicion_jugador[0]=x
            
            if event.key==pygame.K_RIGHT:
              x+=tamano_jugador

            posicion_jugador[0]=x      

    ventana.fill(negro)

    if posicion_enemigo[1]>=0 and posicion_enemigo[1]< alto:
        posicion_enemigo[1]+=20
    else:
        posicion_enemigo[0]=random.randint(0,ancho-tamano_enemigo)
        posicion_enemigo[1]=0

#chocar
    if detecta_colision(posicion_jugador, posicion_enemigo):
        game_over=True

#enemigo
    pygame.draw.rect(ventana, 
                    color_enemigo,(posicion_enemigo[0],
                            posicion_enemigo[1],
                            tamano_enemigo,
                            tamano_enemigo))
            

#dibujar jugador
    pygame.draw.rect(ventana, 
                     color_jugador,(posicion_jugador[0],
                               posicion_jugador[1],
                               tamano_jugador,  
                               tamano_jugador))
    
    tiempo.tick(30)
    pygame.display.update()