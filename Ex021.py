# Faça um programa que abra e reproduza o áudio de um arquivo MP3
from pygame import mixer
mixer.init()
mixer.music.load('música.mp3')
mixer.music.set_volume(0.1)

while True:
    
    print("\nAperte 's' para começar a música")
    print("Aperte 'p' para pausa a música")
    print("Aperte 'r' para despausar a música")
    print("Aperte 'e' para parar a música")
    query = input('\n')

    if query == 's':
        mixer.music.play()
    
    elif query == 'p':
        mixer.music.pause()
    
    elif query == 'r':
        mixer.music.unpause()
    
    elif query == 'e':
        mixer.music.stop()
        break