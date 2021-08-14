import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
    
    for i in range(290,320):
            for j in range(430,480):
                if data[i,j] > 80  :
                    hit("up")
                    return 
    for i in range(290,320):
        for j in range(300,340):
            if data[i,j] > 80  :
                hit("down")
                break
                return 
    return


if __name__== "__main__":
    print("Dino game is about to start in 3 sec")
    time.sleep(3)
    hit("up")
    # while True:
    image = ImageGrab.grab().convert('L')
    data = image.load() # data comes in as an array used to load pixel data 
    # iscollide(data)

    for i in range(250,300):
        for j in range(430,480):
            data[i,j] =  0
    image.show()
            
        

