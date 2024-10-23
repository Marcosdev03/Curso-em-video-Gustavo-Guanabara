import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Mantém o programa rodando até a música terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
