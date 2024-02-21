import pygame
import sys
from funciones import *

#ventana
ventana=pygame.display.set_mode((ancho, alto))
game_over=False
tiempo=pygame.time.Clock()




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