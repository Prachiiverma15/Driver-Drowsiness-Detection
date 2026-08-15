import pygame
import threading

pygame.mixer.init()

def play_sound():
    try:
        pygame.mixer.music.load('data/alert_tone.mp3')
        pygame.mixer.music.play()
    except Exception as e:
        print("Alarm error:", e)

def sound_alarm():
    t = threading.Thread(target=play_sound)
    t.daemon = True
    t.start()