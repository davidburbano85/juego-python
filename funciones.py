import random

tamano_enemigo=50
tamano_jugador=50
ancho=800
alto=600
negro=(0,0,0)


#jugador
posicion_jugador=[ancho/2,alto-tamano_jugador*2]
color_jugador=(255,0,0)

#enemigos
posicion_enemigo=[random.randint(0,ancho-tamano_enemigo),0]
color_enemigo=(0,0,255)
       
def detecta_colision(posicion_jugador, posicion_enemigo):
    jugador_en_x=posicion_jugador[0]
    jugador_en_y=posicion_jugador[1]
    enemigo_x=posicion_enemigo[0]
    enemigo_y=posicion_enemigo[1]

    if(enemigo_x>=jugador_en_x and enemigo_x < (jugador_en_x + tamano_jugador)) or (jugador_en_x >= enemigo_x and jugador_en_x < (enemigo_x + tamano_enemigo)):
        if(enemigo_y >= jugador_en_y and enemigo_y < (jugador_en_y + tamano_jugador)) or(jugador_en_y >= enemigo_x and jugador_en_y<(enemigo_y + tamano_jugador)):
            return True
    return False