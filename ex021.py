#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.init()
if os.path.exists('musica.mp3.mp3'):
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    ck.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')
