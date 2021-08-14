import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
    for i in range(290,320):
        for j in range(300,385):
            if data[i,j] > 60 and data[i,j] < 95  :
                hit("down")
                return 
    for i in range(290,320):
            for j in range(430,480):
                if data[i,j] > 60 data[i,j] < 95  :
                    hit("up")
                    return 
    return


if __name__== "__main__":
    print("Dino game is about to start in 3 sec")
    time.sleep(3)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load() # data comes in as an array used to load pixel data 
        iscollide(data)
    
#     for i in range(250,300):
#         for j in range(290,385):
#             data[i,j] =  0
# image.show()
        
        

