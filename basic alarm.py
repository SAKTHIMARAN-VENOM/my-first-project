import datetime
import time
import pygame
def alarmclock(alarm_time):
    a=alarm_time.split(":") 
    sound="C:/Python/Straw Squeak.mp3"
    while True:
         current_time=datetime.datetime.now().strftime("%H:%M:%S")
         print(current_time)
         
         if current_time==alarm_time:
              print("WAKE UP BIATCH")
              pygame.mixer.init()
              pygame.mixer.music.load(sound)
              pygame.mixer.music.play()
         while pygame.mixer.music.get_busy:
               time.sleep(1)
               break
    
              
             
            
def main():
    alarm_time=input("ENTER THE TIME TO SET ALARM: ")
    alarmclock(alarm_time)
if __name__=='__main__':
       main()
